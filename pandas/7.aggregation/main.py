import pandas as pd

# aggregat function = Reduces a set of values into a single summary value Used to summarize and analyze data often used with 
                    #   groupby() function
                    
df = pd.read_csv('pandas/7.aggregation/pokemon.csv')
print(df.mean(numeric_only=True))