import pandas as pd


data = {
    'Name': ['vivek', 'sujal', 'sushant', 'sahil', 'samarth', 'sai', 'tanvi'], 
    'Age' : [21, 20, 22, 22, 21, 21, 21 ],
    'Scores': [97, 94, 90, 92, 99, 97, 100 ]
}

df = pd.DataFrame(data)


# Adding columns 

# 1. adding column via squarec bracket []

df['gender'] = ['Male', 'Male', 'Male', 'Male','Male', 'Male', 'Female']



# 2. using insert()
# df.insert(loc, 'column_name', 'data')

df.insert(0, 'Id', [1, 2, 3, 4, 5, 6, 7])
print(df)