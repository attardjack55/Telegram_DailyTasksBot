import os
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Load secrets
CLICKUP_TOKEN = os.getenv("CLICKUP_API_TOKEN")
CLICKUP_USER_ID = os.getenv("CLICKUP_USER_ID", "94656814")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Init OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

HEADERS = {"Authorization": CLICKUP_TOKEN}

def get_team_id():
    """Fetch your default Team ID (Workspace)"""
    url = "https://api.clickup.com/api/v2/team"
    res = requests.get(url, headers=HEADERS)
    teams = res.json().get("teams", [])
    if not teams:
        raise Exception("No teams found — check your token.")
    return teams[0]["id"]

def fetch_tasks(team_id, user_id):
    """Fetch tasks assigned to the user that are due today or overdue"""
    url = f"https://api.clickup.com/api/v2/team/{team_id}/task"
    today = datetime.utcnow().replace(tzinfo=timezone.utc)

    params = {
        "assignees[]": user_id,
        "include_closed": "false",
        "subtasks": "true",
        "due_date_lt": int(today.timestamp() * 1000),
    }

    res = requests.get(url, headers=HEADERS, params=params)
    if res.status_code != 200:
        print("❌ Failed to fetch tasks:", res.text)
        return []

    return res.json().get("tasks", [])

def get_task_details(task_id):
    """Fetch task description and comments"""
    url = f"https://api.clickup.com/api/v2/task/{task_id}"
    res = requests.get(url, headers=HEADERS)
    task = res.json()

    # Get comments
    comments_url = f"https://api.clickup.com/api/v2/task/{task_id}/comment"
    comments_res = requests.get(comments_url, headers=HEADERS)
    comments = comments_res.json().get("comments", [])

    # Get latest 3 comments
    comment_texts = [
        f"{c['user']['username']}: {c['comment_text']}"
        for c in comments[-3:]
        if 'comment_text' in c
    ]

    return {
        "title": task.get("name", "Untitled Task"),
        "description": task.get("description", ""),
        "comments": comment_texts,
    }

def summarize_task(task_id):
    """Use OpenAI to summarize a task and recommend next step"""
    details = get_task_details(task_id)
    comments = "\n".join(details["comments"]) if details["comments"] else "None"

    prompt = f"""
You are an expert task manager assistant.

Here is the task:
Title: {details['title']}

Description:
{details['description']}

Recent Comments:
{comments}

Based on this, provide a brief 1-line summary of what this task is about,
and a suggested next action (even if it's to wait, ask, approve, or do something).

Format:
Summary: ...
Next step: ...
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Or use "gpt-3.5-turbo" if preferred
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Error summarizing task {task_id}: {str(e)}"

# ✅ Optional: test it on 3 tasks
if __name__ == "__main__":
    team_id = get_team_id()
    tasks = fetch_tasks(team_id, CLICKUP_USER_ID)

    if not tasks:
        print("🎉 No tasks to summarize")
    else:
        for task in tasks:  # ✅ now processes all tasks
            print(f"\n📝 Task: {task['name']}")
            print(summarize_task(task["id"]))

