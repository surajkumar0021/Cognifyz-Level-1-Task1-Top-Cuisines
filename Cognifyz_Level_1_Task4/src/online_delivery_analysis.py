import pandas as pd
import matplotlib.pyplot as plt
import os

#  Full path to your dataset
csv_file = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\Cognifyz_Level_1_Task4\data\dataset.csv"

#  Read data into DataFrame
data = pd.read_csv(csv_file)

#  Remove rows where essential columns are missing
data = data.dropna(subset=['Has Online delivery', 'Aggregate rating'])

#  Normalize text entries in 'Has Online delivery' column
data['Has Online delivery'] = data['Has Online delivery'].str.strip().str.lower()

# Calculate count and percentage of restaurants offering online delivery
offers_delivery = data[data['Has Online delivery'] == 'yes']
delivery_pct = (len(offers_delivery) / len(data)) * 100

print(f"📦 Percentage of Restaurants with Online Delivery: {delivery_pct:.2f}%")

#  Compare average ratings between delivery options
avg_rating = data.groupby('Has Online delivery')['Aggregate rating'].mean()

print("\n⭐ Average Ratings Based on Delivery Availability:")
for option, rating in avg_rating.items():
    label = "With Delivery" if option == 'yes' else "No Delivery"
    print(f" - {label}: {rating:.2f}")

#  Create a bar chart to compare average ratings
plt.figure(figsize=(8, 5))
avg_rating.plot(kind='bar', color=['#2ecc71', '#e67e22'])
plt.title("Online Delivery vs Average Restaurant Ratings", fontsize=13)
plt.xlabel("Online Delivery Status")
plt.ylabel("Average Rating")
plt.xticks(ticks=[0, 1], labels=["No", "Yes"], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()

#  Save the visual
output_image = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\Cognifyz_Level_1_Task4\output\online_delivery_rating_comparison.png"
os.makedirs(os.path.dirname(output_image), exist_ok=True)
plt.savefig(output_image)
print(f"\n✅ Bar chart saved to: {output_image}")

#  Display the plot
plt.show()
