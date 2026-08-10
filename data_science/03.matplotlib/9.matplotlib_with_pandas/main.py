import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv('data_science/03.matplotlib/9.matplotlib_with_pandas/pokemon.csv')
type_count = data["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values)
plt.show()