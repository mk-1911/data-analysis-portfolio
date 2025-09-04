import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"..\results\q07_engine_type_hp_to_mpg.csv"

df = pd.read_csv(file_path)

pivot = df.pivot(index="cylinders", columns="hp_range", values="avg_mpg")

plt.figure(figsize=(10, 6))
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="Blues")

plt.title("Fuel Efficiency by Engine Cylinders & Horsepower Range", fontsize=14)
plt.xlabel("Horsepower Range")
plt.ylabel("Cylinders")
plt.tight_layout()
plt.show()
