import pandas as pd
import matplotlib.pyplot as plt

file_path = r"..\results\q03_cylinders_vs_mpg.csv"

cylinders_vs_mpg = pd.read_csv(file_path)

plt.figure(figsize = (10,6))

plt.bar(cylinders_vs_mpg["cylinders"].astype(str),
        cylinders_vs_mpg["Average_mpg"],
        color='steelblue', edgecolor='black')

plt.title(" Average MPG by Number of Cylinders", fontsize=14)
plt.xlabel("Cylinders", fontsize=12)
plt.ylabel("Average MPG", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
