import os
import datetime
import pickle
import base64

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def get_calendar_events():
    print("🔄 Starting calendar fetch...")

    # Decode credentials.json from Railway secret if it exists
    creds_b64 = os.getenv("GCAL_CREDENTIALS_B64")
    if creds_b64:
        with open("credentials.json", "wb") as f:
            f.write(base64.b64decode(creds_b64))
        print("🔐 credentials.json generated from environment variable.")

    # Decode token.pickle from Railway secret if it exists
    token_b64 = os.getenv("GCAL_TOKEN_B64")
    if token_b64:
        with open("token.pickle", "wb") as f:
            f.write(base64.b64decode(token_b64))
        print("🔐 token.pickle generated from environment variable.")

    creds = None
    token_path = "token.pickle"

    if os.path.exists(token_path):
        print("✅ Found token.pickle — loading credentials")
        with open(token_path, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("🔁 Refreshing expired credentials")
            creds.refresh(Request())
        else:
            print("🌐 Initiating browser login (or manual code)")
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=8080)

        with open(token_path, "wb") as token:
            pickle.dump(creds, token)
        print("💾 Credentials saved to token.pickle")

    print("📡 Connecting to Google Calendar...")
    service = build("calendar", "v3", credentials=creds)

    now = datetime.datetime.utcnow()
    start_of_day = now.replace(hour=0, minute=0, second=0).isoformat() + "Z"
    end_of_day = now.replace(hour=23, minute=59, second=59).isoformat() + "Z"

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start_of_day,
            timeMax=end_of_day,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])
    print(f"📅 Found {len(events)} event(s) today")

    formatted = []
    for event in events:
        summary = event.get("summary", "No Title")
        start_data = event.get("start", {})
        start = start_data.get("dateTime", start_data.get("date"))

        if "T" in start:
            time = start[11:16]  # Extract HH:MM
        else:
            time = "All Day"

        formatted.append({
            "summary": summary,
            "start_time": time
        })

    return formatted

# Optional test run
if __name__ == "__main__":
    result = get_calendar_events()
    print("\n📋 Today's Events:\n")
    for e in result:
        print(f"- {e['start_time']} → {e['summary']}")
