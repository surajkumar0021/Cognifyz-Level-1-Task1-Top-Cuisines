import pandas as p
import matplotlib.pyplot as m
import seaborn as sns
import os

# manually set path to dataset (double checked in explorer)
datasetLocation = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\cognifyz_level_2_task1\data\dataset.csv"

if not os.path.exists(datasetLocation):
    print(" file not found... check path again or file extension maybe wrong?")
    exit()

# load csv - assuming it's comma separated
try:
    d = p.read_csv(datasetLocation)
    print("\nFile loaded successfully!\n")
except Exception as e:
    print("Error reading CSV file:", str(e))
    exit()

# just to understand structure
print("Columns available:\n", list(d.columns))
print("Here's a random preview:\n", d.sample(4))  # not head – we like variety

# required fields check – maybe casing matters?
if 'Aggregate rating' not in d.columns or 'Votes' not in d.columns:
    print(" Required columns not present. Are they renamed or missing?")
    exit()

# remove any rows with missing data in key columns
filteredData = d[['Aggregate rating', 'Votes']]
filteredData = filteredData.dropna()

# convert Votes to int (just in case it's weird)
try:
    filteredData['Votes'] = filteredData['Votes'].astype('int')
except:
    filteredData['Votes'] = p.to_numeric(filteredData['Votes'], errors='coerce')
    filteredData = filteredData[filteredData['Votes'].notnull()]

print("\nAfter cleaning, total usable rows =", len(filteredData))

# PLOT time
m.figure(figsize=(9.5,5.2))
sns.histplot(filteredData['Aggregate rating'], bins=13, color='tomato', edgecolor='black')
m.title("How Restaurants Are Rated ", fontsize=14)
m.xlabel("Rating Scale", fontsize=11)
m.ylabel("Restaurant Count", fontsize=11)
m.grid(True, linestyle=':', alpha=0.6)

save_here = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\cognifyz_level_2_task1\output\graph_ratings.png"
if not os.path.exists(os.path.dirname(save_here)):
    os.makedirs(os.path.dirname(save_here))
m.savefig(save_here)
m.close()

# Now find most frequent rating – not best way, but works
all_ratings = list(filteredData['Aggregate rating'])
mode_rating = max(set(all_ratings), key = all_ratings.count)
count_mode = all_ratings.count(mode_rating)

print(f"\n Most common rating is {mode_rating} — appears {count_mode} times")

# avg votes – manually using sum and len just to be different
total_votes = sum(filteredData['Votes'])
avg_votes = total_votes / len(filteredData)

print(f"\n🧮 Avg number of votes per restaurant: {round(avg_votes, 1)}")
print(f"\n Graph image saved at: {save_here}")
#ss
