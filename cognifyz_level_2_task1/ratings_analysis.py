# ratings_analysis.py

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import os

# Use your specific dataset path
file_path = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\cognifyz_level_2_task1\data\dataset.csv"

# Check if file exists
if not os.path.exists(file_path):
    print(" Dataset not found. Please check the path.")
    exit()

# Read the CSV
data = pd.read_csv(file_path)

# Show initial rows
print(" Preview of the Data:")
print(data.head())

# Required columns
columns_needed = ['Aggregate rating', 'Votes']

if not all(col in data.columns for col in columns_needed):
    print(" One or more required columns are missing.")
    exit()

# Clean and prepare data
filtered = data[columns_needed].dropna()
filtered['Votes'] = pd.to_numeric(filtered['Votes'], errors='coerce')
filtered = filtered.dropna()

# 1️⃣ Plotting the Rating Distribution
plt.figure(figsize=(9, 5))
sb.histplot(filtered['Aggregate rating'], bins=12, color='skyblue', edgecolor='black')
plt.title("Restaurant Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--')
plt.tight_layout()

# Save the plot
output_plot_path = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\cognifyz_level_2_task1\output\rating_distribution.png"
os.makedirs(os.path.dirname(output_plot_path), exist_ok=True)
plt.savefig(output_plot_path)
plt.close()

# 2️⃣ Most Frequent Rating
rating_stats = filtered['Aggregate rating'].value_counts().sort_values(ascending=False)
most_common_rating = rating_stats.index[0]
occurrence = rating_stats.iloc[0]
print(f"\n⭐ Most common rating: {most_common_rating} ({occurrence} restaurants)")

# 3️⃣ Average Number of Votes
avg_votes = filtered['Votes'].mean()
print(f"\n📈 Average votes per restaurant: {avg_votes:.2f}")

print(f"\n✅ Plot saved to:\n{output_plot_path}")
