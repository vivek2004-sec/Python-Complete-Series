import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data_science/jupyter_notebook/test.csv")
print(df['Age'] == 'NaN')