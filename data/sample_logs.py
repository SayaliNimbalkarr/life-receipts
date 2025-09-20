import csv
import os
from datetime import datetime, timedelta
import random

# -----------------------------
# CONFIGURATION 
# -----------------------------
num_rows = 2000  # Number of rows you want
start_date = datetime(2025, 9, 20)
end_date = datetime(2025, 9, 25)  

activities = [
    ("Reading", "Productive"),
    ("Coding", "Productive"),
    ("Emails", "Productive"),
    ("Meeting", "Productive"),
    ("Gardening", "Productive"),
    ("Volunteering", "Productive"),
    ("Journaling", "Productive"),
    ("Writing", "Productive"),
    ("Coding", "Productive"),
    ("Learning", "Productive"),
    ("Instagram", "Leisure"),
    ("YouTube", "Leisure"),
    ("Netflix", "Leisure"),
    ("Walk", "Leisure"),
    ("Lunch", "Leisure"),
    ("Dinner", "Leisure"),
    ("Breakfast", "Leisure"),
    ("Jogging", "Leisure"),
    ("Draw", "Leisure"),
    ("Photography", "Leisure"),
    ("Puzzles", "Leisure")
]

output_file = "data/sample_logs.csv"
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# -----------------------------
# Ensure output folder exists
# -----------------------------
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# -----------------------------
# Helper function to get random date
# -----------------------------
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# -----------------------------
# Generate CSV rows
# -----------------------------
rows = []
for _ in range(num_rows):
    date = random_date(start_date, end_date)
    activity, category = random.choice(activities)
    
    # Random start time between 6:00 and 22:00
    start_hour = random.randint(6, 21)
    start_minute = random.choice([0, 15, 30, 45])
    start_time = datetime(date.year, date.month, date.day, start_hour, start_minute)
    
    # Random duration 30–90 minutes
    duration = random.randint(30, 90)
    end_time = start_time + timedelta(minutes=duration)
    
    row = [
        start_time.date().isoformat(),
        start_time.time().strftime("%H:%M"),
        end_time.time().strftime("%H:%M"),
        activity,
        category
    ]
    rows.append(row)

# -----------------------------
# Write to CSV
# -----------------------------
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "start_time", "end_time", "activity", "category"])
    writer.writerows(rows)

print(f"CSV file '{output_file}' created successfully with {num_rows} rows!")
