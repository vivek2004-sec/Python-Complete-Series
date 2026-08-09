import pandas as pd

# Filtering : Keeping the rows that match a condition.

df = pd.read_csv('pandas/6.filtering/pokemon.csv')
# tall_pokemon = df[df["Height"] > 2
# heavy_pokemon = df[df["Weight"] > 100]
# legendary_pokemon = df[df["Legendary"] == True]
# water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Grass")]
# grass_pokemon = df[(df["Type1"] == "Grass") | (df["Type2"] == "Water")]
# pokemon = pd.concat([water_pokemon, grass_pokemon])
fire_type = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(fire_type)