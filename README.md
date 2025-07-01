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
