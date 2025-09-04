import pandas as pd
import matplotlib.pyplot as plt

file_path = r"..\results\q06_hp_to_mpg.csv"
hp_to_mpg  = pd.read_csv(file_path)

plt.figure(figsize = (18,6))

plt.barh(hp_to_mpg["model_year"], hp_to_mpg["hp_to_mpg_ratio"], color="steelblue")

plt.title("Top 10 Cars by Horsepower-to-MPG Ratio", fontsize=14)
plt.xlabel("MPG per Horsepower", fontsize=12)
plt.ylabel("Car Make and Model", fontsize=12)

plt.tight_layout
plt.show()