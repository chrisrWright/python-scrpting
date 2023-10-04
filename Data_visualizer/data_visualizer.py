import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Data Loading and Exploration
df = pd.read_csv('data.csv')
print(df.columns)

print(df.head())
print(df.describe())

# Step 2: Data Cleaning
df = df.drop_duplicates()
df = df.dropna()

# Step 3: Exploratory Data Analysis
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')

plt.subplot(132)
plt.hist(df['Income'], bins=20, color='salmon', edgecolor='black')
plt.title('Income Distribution')

plt.subplot(133)
plt.hist(df['Spending_Score'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Spending Score Distribution')

plt.tight_layout()
plt.show()

# Step 4: Data Preprocessing (Scaling)
scaler = StandardScaler()
df[['Age', 'Income', 'Spending_Score']] = scaler.fit_transform(df[['Age', 'Income', 'Spending_Score']])

# Step 5: Customer Segmentation
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(df[['Age', 'Income', 'Spending_Score']])

# Step 6: Cluster Analysis
cluster_means = df.groupby('Cluster').mean()
print(cluster_means)

# Step 7: Data Visualization
plt.scatter(df['Income'], df['Spending_Score'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.title('Customer Segmentation')
plt.show()
