# import required modules
import pandas as pd

# create dataset
df = pd.DataFrame({'Temperature': ['Hot', 'Cold', 'Warm', 'Cold'],
                   })

# display dataset
print(df)

# create dummy variables
print(pd.get_dummies(df))

# create dataset
df = pd.DataFrame({'A': ['hello', 'vignan', 'geeks'],
                   'B': ['vignan', 'hello', 'hello'],
                   'C': [1, 2, 3]})

# display dataset
print(df)

# create dummy variables
print(pd.get_dummies(df))

