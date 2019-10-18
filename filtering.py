#filtering.py

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("train.csv")

df = df[(df["Age"] > 20) | (df["Embarked"] == "Q")]



x = df["Age"]
y = df["Parch"]

plt.scatter(x, y, marker='x')
plt.xlabel("Age")
plt.ylabel("Parch")
plt.xlim(-3,83)
plt.title("{} embarked from Q".format(len(df)))

plt.show()