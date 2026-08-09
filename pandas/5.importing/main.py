import pandas as pd

# csv = comma -seperated values
# json = Javascript object Notaion

# df = pd.read_csv('pandas/5.importing/pokemon.csv')
# print(df.to_string())

df = pd.read_json('pandas/5.importing/pokemon.json')
print(df)