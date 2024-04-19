import pandas as pd
# read csv files
df=pd.read_csv('pokemon_data.csv')

# read excel files
df_excel=pd.read_excel('pokemon_data.xlsx')

# read text files
df_text=pd.read_csv('pokemon_data.txt')

# print entire data
print(df)

# print 3 rows from top
print(df.head(3))

# print 3 rows from below
print(df.tail(3))

# read headers
print(df.columns)

# read each column prints first five of them
print(df['Name'][0:5])

print(df[['Name','HP']])

# print each row
print(df.iloc[2])
print(df.iloc[2:5])

for index,row in df.iterrows():
    print(index,row['Name'])

# print a specific column of a row
print(df.iloc[2,1])

print(df.loc[df['Type 1']=="Fire"])


# get stats about data
print(df.describe())

# sort data
print(df.sort_values('Name'))
print(df.sort_values('Name',ascending=False))
print(df.sort_values(['Name','HP'],ascending=[1,0]))

# making changes to the dataframe
df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
df['Total']=df.iloc[:,4:10].sum(axis=1)
# axis=0 for vertical
print(df['Total'])
print(df)

# dropping a column
df=df.drop(columns=['Generation'])
print(df)

# rearranging columns
cols=list(df.columns.values)
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
print(df.head(5))

# saving the changes
df.to_csv('modified.csv')
