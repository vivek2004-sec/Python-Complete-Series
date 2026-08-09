import pandas as pd

data = [100, 102, 104, 104, 200, 204]

series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f'])
print(series[series >= 200])
# [] -> called subscript operator.


pokemons = ['pikachu', 'balbasaur', 'charizard', 'grey ninja', 'froggy', 'squartle']
series = pd.Series(pokemons)
print(series)