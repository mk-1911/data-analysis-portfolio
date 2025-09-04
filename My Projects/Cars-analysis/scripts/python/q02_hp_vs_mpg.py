import pandas as pd
import matplotlib.pyplot as plt

file_path = r"..\results\q02_hp_vs_mpg.csv"
hp_vs_mpg = pd.read_csv(file_path)


plt.figure(figsize=(10,6))
plt.scatter(hp_vs_mpg['horsepower'], hp_vs_mpg['mpg'], alpha=0.6, color="teal")

plt.title("Horsepower vs MPG", fontsize=14)
plt.xlabel("Horsepower", fontsize=12)
plt.ylabel("Miles Per Gallon (MPG)", fontsize=12)

plt.grid(alpha=0.3)


plt.tight_layout()
plt.show()