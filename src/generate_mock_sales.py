import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
years = [2020, 2021, 2022, 2023]
sales = []

def random_date(year):
    start = datetime(year, 1, 1)
    end = datetime(year, 12, 31)
    return start + timedelta(days=random.randint(0, 364))

def generate_sales(year, product, count, price_range, female_ratio):
    for i in range(count):
        gender = 'F' if random.random() < female_ratio else 'M'
        price = random.randint(*price_range) if isinstance(price_range, tuple) else price_range
        sales.append({
            'sale_id': f"S{len(sales)+1:05d}",
            'date': random_date(year).strftime('%Y-%m-%d'),
            'product': product,
            'price': price,
            'gender': gender,
            'year': year
        })

# Generate sales
for year in years:
    generate_sales(year, 'Print', 20, (25, 50), 0.4)
    generate_sales(year, 'Pin', 30, 3, 0.5)
    generate_sales(year, 'T-Shirt', random.randint(20, 30), (15, 20), 0.3)  # 70% male = 30% female

# Save to CSV
df = pd.DataFrame(sales)
df.to_csv('data/sales_mock.csv', index=False)
print(f"Generated {len(df)} sales records.")