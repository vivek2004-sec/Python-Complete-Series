import pandas as pd

# aggregat function = Reduces a set of values into a single summary value Used to summarize and analyze data often used with 
                    #   groupby() function
                    
df = pd.read_csv('pandas/7.aggregation/pokemon.csv')

#  Whole DataFrame
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# For a single Column 

# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

group = df.groupby("Type1")
# print(group["Name"].count())
# print(group["Height"].sum())
# print(group["Height"].min())
print(group["Height"].max())