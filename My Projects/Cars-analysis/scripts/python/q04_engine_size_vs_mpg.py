import pandas as pd
import matplotlib.pyplot as plt

file_path = r"..\results\q04_engine_size_vs_mpg.csv"

engine_size_vs_mpg = pd.read_csv(file_path)

plt.figure(figsize=(10,6))

plt.scatter(engine_size_vs_mpg["engine_size"], engine_size_vs_mpg["mpg"], alpha=0.6, color="teal")

plt.title("Engine Size vs MPG", fontsize=14)
plt.xlabel("Engine Size", fontsize=12)
plt.ylabel("MPG", fontsize=12)

plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()