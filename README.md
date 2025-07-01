# 🧠 Telegram Daily Tasks Bot

An automated Python bot that sends you a smart daily summary of:

- 📅 Google Calendar meetings  
- ✅ ClickUp tasks (due & overdue)  
- 📝 AI-powered task summaries (via OpenAI)  
- 📲 Delivered straight to Telegram via a custom bot  

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
```

**Example `.env` file:**

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
CLICKUP_API_TOKEN=your_clickup_api_token
CLICKUP_USER_ID=your_clickup_user_id
OPENAI_API_KEY=your_openai_key
```

Also place your `credentials.json` file (Google Calendar OAuth) in the root directory.

---

## 🧪 Run It Locally

```bash
python3 daily_summary.py
```

---

## 🗓️ Automate It in the Cloud

You can schedule this to run daily at 8AM via:

- [Render Cron Jobs](https://render.com/docs/cron-jobs)  
- [Railway](https://railway.app)  
- [PythonAnywhere](https://www.pythonanywhere.com/)  

This will make sure your bot works even when your laptop is turned off.

---

## 📬 Sample Output (Telegram)

```
🗓️ Today’s Events
- 12:00 → Liquigas Survey Review
- 16:30 → Client Alignment
- 17:30 → Call Cesco and Kira

📌 ClickUp Tasks Summary

📝 *Schedule IG Internal Content*
Summary: This task involves arranging the schedule for Instagram content for TGB.
Next step: Begin by reviewing the content and create a timeline for posting.

📝 *Launch Checklist*
Summary: This task involves creating a launch checklist for Facebook Ads.
Next step: Draft components needed and confirm campaign setup.
```

---

## 👤 Created By

[Jack Attard Cassar](https://github.com/attardjack55) • The Growth Bully Ltd.
