import pandas as pd

df = pd.read_csv('salaries.csv')

print(df[df['Age'] > 30])
