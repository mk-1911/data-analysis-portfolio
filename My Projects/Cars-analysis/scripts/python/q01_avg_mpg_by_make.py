import pandas as pd
import matplotlib.pyplot as plt

file_path = r"..\results\q01_avg_mpg_by_make.csv"
avg_mpg_by_make = pd.read_csv(file_path)

plt.figure(figsize=(12,6))

plt.bar(avg_mpg_by_make['make'], avg_mpg_by_make['Average_mpg'], color="skyblue")

plt.xticks(rotation=45, ha="right")

plt.title('Average MPG by Make', fontsize=14)
plt.xlabel('Car Make', fontsize=12)
plt.ylabel('Average MPG', fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()