import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

# ✅ Load the dataset using full path
data_path = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\Cognifyz_Level_1_Task\data\dataset.csv"
df = pd.read_csv(data_path)

# ✅ Drop missing values from 'Cuisines'
df = df[df['Cuisines'].notna()]

# ✅ Count individual cuisines
cuisine_counter = Counter()
for cuisines in df['Cuisines']:
    for cuisine in [c.strip() for c in cuisines.split(',')]:
        cuisine_counter[cuisine] += 1

# ✅ Get top 3 cuisines
top_3 = cuisine_counter.most_common(3)

print("Top 3 Cuisines:")
for cuisine, count in top_3:
    print(f"{cuisine}: {count} restaurants")

# ✅ Total number of restaurants
total_restaurants = len(df)

# ✅ Calculate percentage
print("\nPercentages:")
for cuisine, count in top_3:
    percentage = (count / total_restaurants) * 100
    print(f"{cuisine}: {percentage:.2f}%")

# ✅ Plot bar chart
cuisines, counts = zip(*top_3)
plt.figure(figsize=(8, 5))
plt.bar(cuisines, counts, color='skyblue')
plt.title("Top 3 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.tight_layout()

# ✅ Save the plot using absolute path
output_path = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\Cognifyz_Level_1_Task\output\cuisine_plot.png"

# Make sure output folder exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

plt.savefig(output_path)
print(f"\nBar chart saved to {output_path}")
plt.show()
