import csv

data = [
    ["Name", "Email", "Task", "Date"],
    ["Karthik", "karthikgr0819@gmail.com", "Complete Python automation script", "2025-06-19"],
    ["Prani", "usernamecopied19@gmail.com", "Join standup meeting at 10 AM", "2025-06-18"],
    ["Sinchana", "karthikgr0819@gmail.com", "Review code and push to GitHub", "2025-06-19"],
    ["Madhuri", "usernamecopied19@gmail.com", "Submit project documentation", "2025-06-19"],
    ["Sinchana", "19.heyyou@gmail.com", "Test email automation feature", "2025-06-18"],
    ["Lavanya", "usernamecopied19@gmail.com", "Prepare slides for presentation", "2025-06-19"],
]

with open("reminders.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created.")
