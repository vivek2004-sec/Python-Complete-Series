import pandas as pd


# head(n) : Gives first n rows of dataset
# tail(n) : returns last n rows of dataset

df = pd.read_csv("data_science/02.pandas/4.dataframes/pokemon.csv")

print(df.head(10))
print(df.tail(10))