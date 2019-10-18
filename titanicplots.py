#titanicplots.py

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("train.csv")

df.drop(["Cabin"], axis=1, inplace=True)

df.dropna(inplace=True)

print(df.info())

x = df["Age"]
y = df["Parch"]

plt.scatter(x, y, marker='x')
plt.xlabel("Age")
plt.ylabel("Parch")

plt.show()