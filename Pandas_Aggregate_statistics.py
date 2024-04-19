import pandas as pd
# read csv files
df=pd.read_csv('modified.csv')

print(df.groupby(['Type 1']).mean())