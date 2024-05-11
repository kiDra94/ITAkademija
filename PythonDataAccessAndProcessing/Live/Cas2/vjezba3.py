import pandas as pd

data = pd.read_csv('calories.csv', header=0)
print(data.shape)
null_df = data.isnull()
print(null_df.to_string()) #141,118...
for i in data['Calories']:
    if str(i) == 'nan':
        print(i)
data = data.dropna()
print(data.shape)

lista = [4,6,8,9,1]
s = "".join(str(i) + " " for i in lista)
print(s)

d = {"a" : 1, "b" : 2}
print(d["a"])
