import pandas as pd

# csv = comma -seperated values
# json = Javascript object Notaion

# df = pd.read_csv('pandas/5.importing/pokemon.csv')
# print(df.to_string())

# df = pd.read_json('pandas/5.importing/pokemon.json')
# print(df.to_string())


# Selection

# 1.selection by column

df = pd.read_csv('pandas/5.importing_and_selecting/pokemon.csv', index_col='Name')
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[['Name', 'Weight', 'Height']].to_string())

# 2. Selction by rows
# print(df.loc['Charizard':"Blastoise", ["Height", "Weight"]])
# print(df.iloc[0:15:2, 0:3])

pokemon = input("Enter pokemon name: ")

try:
    print(df.loc[pokemon])
    
except KeyError:
    print(f"{pokemon} not found.")