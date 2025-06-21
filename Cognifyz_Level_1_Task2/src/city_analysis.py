import pandas as pd
import matplotlib.pyplot as plt
import os

# ✅ Define relative path to dataset
data_path = os.path.join("..", "data", "dataset.csv")

# ✅ Load the dataset
df = pd.read_csv(data_path)

# ✅ Clean missing values
df = df[df['City'].notna()]
df = df[df['Aggregate rating'].notna()]

# ✅ 1. City with the highest number of restaurants
city_counts = df['City'].value_counts()
top_city = city_counts.idxmax()
print(f"City with the highest number of restaurants: {top_city} ({city_counts.max()} restaurants)")

# ✅ 2. Average rating for each city
city_avg_ratings = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)
print("\nTop 10 Cities by Average Rating:")
print(city_avg_ratings.head(10))

# ✅ 3. City with highest average rating
highest_avg_city = city_avg_ratings.idxmax()
print(f"\nCity with highest average rating: {highest_avg_city} ({city_avg_ratings.max():.2f})")

# ✅ 4. Plot top 10 cities
plt.figure(figsize=(10, 6))
city_avg_ratings.head(10).plot(kind='bar', color='orange')
plt.title("Top 10 Cities by Average Restaurant Rating")
plt.xlabel("City")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.tight_layout()

# ✅ 5. Save chart
output_path = os.path.join("..", "output", "city_analysis.png")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)
print(f"\nBar chart saved to {output_path}")
plt.show()
