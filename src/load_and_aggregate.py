import pandas as pd

# Load extended appointment data
df = pd.read_csv('data/appointments_extended.csv')

# Aggregate client-level features
client_summary = df.groupby('client_id').agg({
    'gender': 'first',
    'age': 'first',
    'style': lambda x: x.value_counts().idxmax(),
    'price': 'sum',
    'appointment_id': 'count',
    'location': 'first'
}).rename(columns={
    'price': 'total_spent',
    'appointment_id': 'num_appointments'
}).reset_index()

# Encode gender and style
client_summary['gender_encoded'] = client_summary['gender'].map({'F': 0, 'M': 1})
client_summary['style_encoded'] = client_summary['style'].map({'Fineline': 0, 'Blackwork': 1})

# Save client profile
client_summary.to_csv('data/client_profile.csv', index=False)
print("Client profile saved.")