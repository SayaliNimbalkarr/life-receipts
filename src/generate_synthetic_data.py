import pandas as pd
import random, datetime

activities = ["Work", "Study", "Exercise", "Leisure", "Sleep"]

rows = []
for day in range(7):
    date = (datetime.date.today() - datetime.timedelta(days=day)).isoformat()
    for act in activities:
        rows.append({
            "date": date,
            "activity": act,
            "duration_hrs": round(random.uniform(0.5, 4.0), 1)
        })

df = pd.DataFrame(rows)
df.to_csv("../data/sample_week.csv", index=False)
print("Sample data saved to data/sample_week.csv")
