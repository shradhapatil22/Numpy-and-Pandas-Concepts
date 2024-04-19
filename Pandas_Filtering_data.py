import pandas as pd
import re


# read csv files
df=pd.read_csv('pokemon_data.csv')

# filtering data with single condition
print(df.loc[df['Type 1']=='Grass'])

# filtering data with multiple conditions
print(df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')])

# # filtering data with multiple or conditions
# df2=df.loc[(df['Type 1']=='Grass') | (df['Type 2']=='Poison')]
# df2=df2.reset_index()
# df2.to_csv('filtering_demo.csv')

df2=df.loc[(df['Type 1']=='Grass') | (df['Type 2']=='Poison')]
print(df2[['Type 1','Type 2']])

# filtering a substring
df3=df.loc[df['Name'].str.contains('Mega')]
print(df3)

# filtering not contain substring
df3=df.loc[~df['Name'].str.contains('Mega')]
print(df3)

# using regular expressions
df3=df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
print(df3)

# starts with a particular substring
df3=df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(df3)