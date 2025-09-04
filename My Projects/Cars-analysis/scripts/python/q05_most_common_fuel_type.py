import pandas as pd
import matplotlib.pyplot as plt

file_path = r"..\results\q05_most_common_fuel_type.csv"

common_fuel_type = pd.read_csv(file_path)

# Bar Chart to show Average MPG by Fuel Type
plt.figure(figsize = (12,6))
plt.bar(common_fuel_type["fuel_type"], common_fuel_type["Average_mpg"],
        color="steelblue", edgecolor = "black")

plt.title("Average MPG by Fuel Type", fontsize = 14)
plt.xlabel("Fuel Type", fontsize = 12)
plt.ylabel("Average MPG", fontsize = 12)

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Bar Chart to show Count Distribution of Fuel types
plt.figure(figsize = (8,5))
bars = plt.bar(common_fuel_type["fuel_type"], common_fuel_type["count"], color="#4682B4")
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 20, f'{height}', ha='center', fontsize=10)

plt.title("Fuel Type Distribution", fontsize = 14)
plt.ylabel("Count")
plt.show()

