import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
years_london = [2021, 2022, 2023]
years_turin = [2024, 2025]
weekdays_london = [1, 2, 3, 4, 5]  # Tue–Sat
sundays_london = [6]               # Sunday
appointments = []

# Helper functions
def random_price(style, year):
    if year in years_london:
        return random.randint(180, 240) if style == 'Fineline' else random.randint(300, 500)
    else:
        return random.randint(120, 200) if style == 'Fineline' else random.randint(300, 500)

def random_style(year):
    if year in years_london:
        return 'Fineline' if random.random() < 0.8 else 'Blackwork'
    else:
        return 'Blackwork' if random.random() < 0.9 else 'Fineline'

def random_gender(year):
    if year in years_london:
        return 'F' if random.random() < 0.85 else 'M'
    else:
        return 'F' if random.random() < 0.6 else 'M'

def generate_appointments(year, location, daily_count, days):
    date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    count = 0
    while date <= end_date:
        if date.weekday() in days:
            for _ in range(daily_count):
                style = random_style(year)
                gender = random_gender(year)
                age = random.randint(20, 40)
                price = random_price(style, year)
                appointments.append({
                    'appointment_id': f"A{count+1:05d}",
                    'date': date.strftime('%Y-%m-%d'),
                    'client_id': f"C{count+1:05d}",
                    'gender': gender,
                    'age': age,
                    'style': style,
                    'price': price,
                    'artist': 'monsternarii',
                    'location': location
                })
                count += 1
        date += timedelta(days=1)

# Generate London data (2021–2023)
for year in years_london:
    generate_appointments(year, 'London-UK', 4, weekdays_london)
    generate_appointments(year, 'London-UK', 2, sundays_london)

# Generate Turin data (2024–2025)
for year in years_turin:
    generate_appointments(year, 'Turin-Italy', 2, [2])  # 2 tattoos every Wednesday

# Save to CSV
df = pd.DataFrame(appointments)
df.to_csv('data/sales_mock.csv', index=False)
print(f"Generated {len(df)} appointments.")