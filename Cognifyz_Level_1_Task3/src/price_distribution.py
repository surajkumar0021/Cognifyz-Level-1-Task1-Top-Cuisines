import pandas as pd
import matplotlib.pyplot as plt
import os

#  Path to the dataset (absolute)
csv_path = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\Cognifyz_Level_1_Task3\data\dataset.csv"

#  Read the CSV file into a DataFrame
restaurant_data = pd.read_csv(csv_path)

#  Filter out missing entries in 'Price range'
filtered_data = restaurant_data.dropna(subset=['Price range'])

#  Group by price range and count entries
range_distribution = filtered_data['Price range'].value_counts().sort_index()

#  Calculate percentage share of each category
total = range_distribution.sum()
percent_distribution = (range_distribution / total) * 100

#  Display distribution stats
print("\n📊 Percentage of Restaurants in Each Price Range:")
for range_cat, percent in percent_distribution.items():
    print(f" - Price Range {range_cat}: {percent:.2f}%")

#  Plotting the distribution
plt.figure(figsize=(9, 6))
plt.bar(range_distribution.index.astype(str), range_distribution.values, color='#4db8ff')
plt.title("Restaurant Price Range Distribution", fontsize=14)
plt.xlabel("Price Range Category")
plt.ylabel("Number of Restaurants")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

#  Save the figure
save_path = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\Cognifyz_Level_1_Task3\output\price_range_distribution.png"
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)
print(f"\n✅ Distribution chart saved at: {save_path}")

# Show plot
plt.show()
