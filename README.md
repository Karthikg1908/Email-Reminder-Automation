# 📧 Email Reminder Automation Script

This Python automation project sends email reminders based on tasks and dates listed in a CSV file. It uses the **smtplib** and **email** libraries to send emails and helps automate the process of reminding users about their scheduled tasks.

---

## 🧠 Project Purpose

This project was built as part of a Python automation interview to showcase skills in:
- Working with CSV files
- Email automation with Gmail SMTP
- Date-based logic using Python's `datetime` module
- Writing clean, modular Python code

---

## 📋 Features

- ✅ Reads task reminders from a CSV file
- 📅 Checks for tasks scheduled **for today**
- 📤 Sends personalized email reminders
- 🛡️ Secure login using Gmail App Password

---

## 🛠️ Requirements

- Python 3.x
- Gmail account with [App Password enabled](https://support.google.com/accounts/answer/185833?hl=en)
- Internet connection

---

## 🗂️ Files Included

- reminders.csv – CSV file containing user data, task, and date.
- email_reminder.py – Main script to check for today's tasks and send email reminders.
- generate_csv.py – Helper script to create a sample reminders.csv file.
