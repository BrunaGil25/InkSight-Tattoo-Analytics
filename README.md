# InkSight: Tattoo Studio Analytics Dashboard
## 🎯 Project Overview
InkSight is a data-driven dashboard built for tattoo artists and creative professionals to understand client behavior, optimize services, and forecast revenue. Originally designed for a tattoo artist who worked in London from 2020-2023 and relocated to Italy in 2024, this project uses mock data to preserve confidentiality while showcasing advanced analytics capabilities.
Whether you're managing appointments, segmenting clients, tracking product sales, or planning seasonal promotions — InkSight helps you make smarter, faster decisions.

---

## 🚀 Features
- 📆 Year & Month: Appointment volume and spending trends
- 🌍 Location: Geographic distribution of clients
- 🧑‍🎨 Segmentation: Behavioral clusters by spending, style, and gender
- 📊 Style & Age: Tattoo preferences and age profiles
- 🛍️ Sales: Product sales breakdown and gender insights
- 📈 Forecasts & Stats: Descriptive statistics and revenue projections
All visualizations are interactive and built with Streamlit, using real-time data pipelines and predictive models.

---

## 🧰 Technologies Used
| Category | Tools & Libraries | 
| Dashboard  | streamlit, matplotlib, seaborn | 
| Data Processing | pandas, numpy | 
| Machine Learning | scikit-learn (Linear Regression) | 
| Clustering | KMeans (optional for segmentation) | 
| File format | .csv for mock and user-uploaded data| 

---

## 📁 File Structure
```text
INKSIGHT/
├── dashboard/
│   └── app.py                      # Streamlit dashboard with 6 tabs
├── data/
│   ├── appointments_extended.csv   # Mock appointment data
│   ├── client_profile.csv          # Raw client demographics (optional)
│   ├── client_segments.csv         # Segmented client clusters
│   └── sales_mock.csv              # Product sales data (prints, pins, t-shirts)
├── notebooks/
│   ├── client_segmentation.ipynb   # KMeans clustering and profiling
│   ├── sales_analysis.ipynb        # Product sales breakdown and trends
│   └── statistical_analysis.ipynb  # Descriptive stats and revenue forecasting
├── reports/
│   └── InkSight_analysis_report.md # Markdown summary of insights
├── src/
│   ├── generate_mock_appointments.py # Synthetic appointment generator
│   ├── generate_mock_sales.py        # Synthetic product sales generator
│   ├── load_and_aggregate.py         # Data loading and preprocessing
│   └── segment_clients.py            # Clustering logic and segment labeling
├── README.md
└── requirements.txt
```

---

## 📥 Installation
```bash
- Clone the repository:
git clone https://github.com/BrunaGil25/InkSight.git
cd InkSight
```
- Install dependencies:
```bash
pip install -r requirements.txt
```
- Run the dashboard:
```bash
streamlit run dashboard/app.py
```

---

## 📤 Upload Your Own Data
You can replace the mock data with your own studio records:
- Format your files to match the structure of the mock datasets:
- appointments_extended.csv: includes date, price, style, gender, location, client_id, appointment_id
- client_segments.csv: includes client_id, segment, num_appointments, total_spent, style, gender, age
- sales_mock.csv: includes sale_id, date, product, price, gender, year
- Save your files in the data/ folder using the same filenames.
- Restart the dashboard to load your data into all visualizations and analytics.
⚠️ Ensure your columns are clean and consistent to avoid errors.



## 📈 Why This Project Matters
Tattoo studios often rely on intuition and experience to manage clients and pricing. InkSight transforms that intuition into data-backed strategy, helping artists:
- Identify high-value clients and loyalty patterns
- Optimize pricing and style offerings
- Forecast revenue and plan seasonal campaigns
- Make confident decisions with visual clarity
This project bridges artistry and analytics, empowering creative professionals to thrive in competitive markets.

## 👩‍💻 Author
Made by Bruna Gil. Data-driven, clean, and powerful. 🔗https://github.com/BrunaGil25 | 🔗 https://www.linkedin.com/in/bruna-gil-garcia-80656069/



