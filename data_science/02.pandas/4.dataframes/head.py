import pandas as pd


# head(n) : Gives first n rows of dataset
# tail(n) : returns last n rows of dataset
# info() : gives the information about the dataset
# describe() : describes  numerical data of the  dataset.

df = pd.read_csv("data_science/02.pandas/4.dataframes/pokemon.csv")

# print(df.head(10))
# print(df.tail(10))
# print(df.info())
# print(df.describe())


data = {
    'Name': ['vivek', 'sujal', 'sushant', 'sahil', 'samarth', 'sai', 'tanvi'], 
    'Age' : [21, 20, 22, 22, 21, 21, 21 ],
    'Scores': [97, 94, 90, 92, 99, 97, 100 ]
}

# df = pd.DataFrame(data)
# print(df)
# print('The descriptive data: ')
# print(df.describe())
print(df.shape)
print(df.columns)