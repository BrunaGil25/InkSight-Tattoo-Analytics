import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LinearRegression

# Load datasets
appointments = pd.read_csv('data/appointments_extended.csv')
segments = pd.read_csv('data/client_segments.csv')
sales = pd.read_csv('data/sales_mock.csv')

# Preprocessing
appointments['date'] = pd.to_datetime(appointments['date'])
appointments['year'] = appointments['date'].dt.year
appointments['month'] = appointments['date'].dt.to_period('M')

sales['date'] = pd.to_datetime(sales['date'])
sales['year'] = sales['date'].dt.year

# Streamlit layout
st.set_page_config(page_title="InkSight Dashboard", layout="wide")
st.title("InkSight: Tattoo Studio Analytics Dashboard")
st.markdown("Visual insights into client behavior, segmentation, product sales, and revenue forecasting.")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📆 Year & Month", "🌍 Location", "🧑‍🎨 Segmentation", "📊 Style & Age", "🛍️ Sales", "📈 Forecasts & Stats"
])

# 📆 Tab 1: Year & Month
with tab1:
    st.subheader("Total Appointments per Year")
    yearly_counts = appointments.groupby('year')['appointment_id'].count()
    fig1, ax1 = plt.subplots()
    sns.barplot(x=yearly_counts.index, y=yearly_counts.values, palette='Blues', ax=ax1)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Appointments")
    st.pyplot(fig1)

    st.subheader("Monthly Spending Over Time")
    monthly_spending = appointments.groupby('month')['price'].sum()
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    monthly_spending.plot(kind='line', marker='o', color='purple', ax=ax2)
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Total Spent (€)")
    st.pyplot(fig2)

# 🌍 Tab 2: Location
with tab2:
    st.subheader("Appointment Distribution by Location")
    location_counts = appointments['location'].value_counts()
    fig3, ax3 = plt.subplots()
    location_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['gold', 'lightblue'], ax=ax3)
    ax3.set_ylabel('')
    st.pyplot(fig3)

# 🧑‍🎨 Tab 3: Segmentation
with tab3:
    st.subheader("Client Segmentation: Appointments vs Spending")
    fig4, ax4 = plt.subplots()
    sns.scatterplot(data=segments, x='num_appointments', y='total_spent',
                    hue='segment', style='gender', palette='Set2', ax=ax4)
    ax4.set_xlabel("Appointments")
    ax4.set_ylabel("Total Spent (€)")
    st.pyplot(fig4)

# 📊 Tab 4: Style & Age
with tab4:
    st.subheader("Age Distribution by Segment")
    fig5, ax5 = plt.subplots()
    sns.boxplot(data=segments, x='segment', y='age', palette='Set2', ax=ax5)
    ax5.set_xlabel("Segment")
    ax5.set_ylabel("Age")
    st.pyplot(fig5)

    st.subheader("Tattoo Style Distribution by Segment")
    style_counts = segments.groupby(['segment', 'style']).size().unstack().fillna(0)
    fig6, ax6 = plt.subplots()
    style_counts.plot(kind='bar', stacked=True, colormap='Set2', ax=ax6)
    ax6.set_xlabel("Segment")
    ax6.set_ylabel("Client Count")
    st.pyplot(fig6)

# 🛍️ Tab 5: Sales Analytics
with tab5:
    st.subheader("Total Sales per Product")
    product_counts = sales['product'].value_counts()
    fig7, ax7 = plt.subplots()
    sns.barplot(x=product_counts.index, y=product_counts.values, palette='Set2', ax=ax7)
    ax7.set_xlabel("Product")
    ax7.set_ylabel("Units Sold")
    st.pyplot(fig7)

    st.subheader("Sales Volume by Year and Product")
    year_product = sales.groupby(['year', 'product']).size().unstack().fillna(0)
    fig8, ax8 = plt.subplots()
    year_product.plot(kind='bar', stacked=True, colormap='Set2', ax=ax8)
    ax8.set_xlabel("Year")
    ax8.set_ylabel("Units Sold")
    st.pyplot(fig8)

    st.subheader("Gender Distribution by Product")
    gender_product = sales.groupby(['product', 'gender']).size().unstack().fillna(0)
    fig9, ax9 = plt.subplots()
    gender_product.plot(kind='bar', stacked=True, colormap='coolwarm', ax=ax9)
    ax9.set_xlabel("Product")
    ax9.set_ylabel("Units Sold")
    st.pyplot(fig9)

    st.subheader("Price Distribution by Product")
    fig10, ax10 = plt.subplots()
    sns.boxplot(data=sales, x='product', y='price', palette='Set2', ax=ax10)
    ax10.set_xlabel("Product")
    ax10.set_ylabel("Price (€)")
    st.pyplot(fig10)

# 📈 Tab 6: Forecasts & Stats
with tab6:
    st.subheader("Descriptive Statistics")
    st.write(appointments[['price', 'age']].describe())

    st.subheader("Gender and Style Distribution")
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(appointments['gender'].value_counts())
    with col2:
        st.bar_chart(appointments['style'].value_counts())

    st.subheader("Correlation Matrix")
    df_encoded = appointments.copy()
    df_encoded['gender'] = df_encoded['gender'].map({'F': 0, 'M': 1})
    df_encoded['style'] = df_encoded['style'].map({'Fineline': 0, 'Blackwork': 1})
    corr = df_encoded[['price', 'age', 'gender', 'style']].corr()
    fig11, ax11 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax11)
    st.pyplot(fig11)

    st.subheader("Monthly Revenue Forecast")
    monthly_revenue = appointments.groupby(appointments['date'].dt.to_period('M'))['price'].sum().reset_index()
    monthly_revenue['month_num'] = np.arange(len(monthly_revenue))
    X = monthly_revenue[['month_num']]
    y = monthly_revenue['price']
    model = LinearRegression()
    model.fit(X, y)
    future_months = pd.DataFrame({'month_num': np.arange(len(monthly_revenue), len(monthly_revenue)+6)})
    future_preds = model.predict(future_months)

    fig12, ax12 = plt.subplots()
    ax12.plot(monthly_revenue['month_num'], y, label='Actual')
    ax12.plot(future_months['month_num'], future_preds, label='Forecast', linestyle='--')
    ax12.set_title('Revenue Forecast (Next 6 Months)')
    ax12.set_xlabel('Month Index')
    ax12.set_ylabel('Revenue (€)')
    ax12.legend()
    st.pyplot(fig12)
