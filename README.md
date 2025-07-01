# 🧠 Telegram Daily Tasks Bot

An automated Python bot that sends you a smart daily summary of:

- 📅 Google Calendar meetings
- ✅ ClickUp tasks (due & overdue)
- 📝 AI-powered task summaries (via OpenAI)
- 📲 Delivered straight to your Telegram via bot

---

## 🚀 Features

- Runs automatically at 8AM (via cloud scheduler)
- Reads tasks assigned to **you** from ClickUp
- Fetches today’s events from Google Calendar
- Summarizes each task using GPT
- Sends everything to Telegram — fully mobile-first

---

## 📁 Tech Stack

- Python 3.11
- Telegram Bot API
- Google Calendar API
- ClickUp REST API
- OpenAI (for task summarization)
- `.env` secrets for secure configuration
- Hosted via Render (or Railway, PythonAnywhere)

---

## 🛠️ Setup (Local)

```bash
# Clone the repo
git clone https://github.com/attardjack55/Telegram_DailyTasksBot.git
cd Telegram_DailyTasksBot

# Create a .env file
touch .env
--
Example .env file:

env
Copy
Edit
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
CLICKUP_API_TOKEN=your_clickup_token
CLICKUP_USER_ID=your_clickup_user_id
OPENAI_API_KEY=your_openai_key
Also place your credentials.json for Google Calendar in the same directory.

🧪 Run It Locally
bash
Copy
Edit
python3 daily_summary.py
🗓️ Automate It in the Cloud
You can schedule this to run daily at 8AM via:

Render Cron Job

Railway

PythonAnywhere

👤 Created By
Jack Attard Cassar • The Growth Bully Ltd.

yaml
Copy
Edit

---

Copy that into a file named `README.md` in your project, then:

```bash
git add README.md
git commit -m "Add README"
git push origin main
