import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load client profile
df = pd.read_csv('data/client_profile.csv')

# Select features
features = ['num_appointments', 'total_spent', 'age', 'gender_encoded', 'style_encoded']
X = df[features]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['segment'] = kmeans.fit_predict(X_scaled)

# Save segmented data
df.to_csv('data/client_segments.csv', index=False)
print("Client segments saved.")