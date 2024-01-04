import matplotlib.pyplot as plt
import pandas as pd

# Load data from the extended CSV file
data = pd.read_csv('extended_business_data.csv')

# Plotting the bar chart with grouped data
fig, ax = plt.subplots(figsize=(10, 6))

# Grouping data by Department and Category, and summing the values
grouped_data = data.groupby(['Department', 'Category'])['Value'].sum().unstack()
grouped_data.plot(kind='bar', ax=ax, colormap='viridis', alpha=0.7)

plt.title('Business Performance by Category and Department')
plt.xlabel('Business Categories')
plt.ylabel('Performance Values')
plt.legend(title='Department', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
