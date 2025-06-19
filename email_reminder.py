import csv
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body, user_name):
    sender_email = "# Use your Email id here"
    sender_password = "# Use your app password here"  

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"✅ Email sent successfully to {user_name} ({to_email})")
    except Exception as e:
        print(f"❌ Failed to send email to {user_name} ({to_email}). Error: {e}")

def check_reminders():
    today = datetime.today().strftime('%Y-%m-%d')
    emails_sent = 0  # Counter

    with open("reminders.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"] == today:
                subject = f"Reminder: {row['Task']}"
                body = (
                    f"Hi {row['Name']},\n\n"
                    f"This is a reminder for your task: {row['Task']} scheduled for today.\n\n"
                    "Regards,\nReminder Bot"
                )
                send_email(row["Email"], subject, body, row["Name"])
                emails_sent += 1

    if emails_sent > 0:
        print(f"\n✅ All {emails_sent} email(s) sent successfully.")
    else:
        print("\n📭 No reminders scheduled for today.")

if __name__ == "__main__":
    check_reminders()
