import os
from dotenv import load_dotenv
from telegram import send_telegram_message  # Custom helper
from google_calendar import get_calendar_events
from clickup import get_team_id, fetch_tasks, summarize_task, CLICKUP_USER_ID

load_dotenv()

# --- FORMATTERS ---

def format_calendar_events(events):
    if not events:
        return "🎉 No events in Google Calendar today."

    lines = ["🗓️ *Today’s Events*"]
    for event in events:
        summary = event.get("summary", "Untitled")
        time = event.get("start_time", "⏰")
        lines.append(f"- {time} → {summary}")
    return "\n".join(lines)

def format_clickup_summary(tasks):
    if not tasks:
        return "✅ No due or overdue ClickUp tasks."

    lines = ["📌 *ClickUp Tasks Summary*"]
    for task in tasks:
        name = task["name"]
        lines.append(f"\n📝 *{name}*")
        try:
            summary = summarize_task(task["id"])
            lines.append(summary)
        except Exception as e:
            lines.append(f"⚠️ Error summarizing: {e}")
    return "\n".join(lines)

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    print("📆 Fetching Google Calendar events...")
    events = get_calendar_events()

    print("📋 Fetching ClickUp tasks...")
    team_id = get_team_id()
    tasks = fetch_tasks(team_id, CLICKUP_USER_ID)

    print("🧠 Formatting message...")
    calendar_section = format_calendar_events(events)
    clickup_section = format_clickup_summary(tasks)

    final_message = f"{calendar_section}\n\n{clickup_section}"

    print("📤 Sending to Telegram...")
    send_telegram_message(final_message)
    print("✅ Done.")
# Trigger redeploy
