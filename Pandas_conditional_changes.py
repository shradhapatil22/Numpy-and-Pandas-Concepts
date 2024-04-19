import pandas as pd
# read csv files
df=pd.read_csv('pokemon_data.csv')

# change valuse of a column in a row
# print((df.loc[df['Type 1'] == 'Fire','Type 1']='Flamer'))

df.loc[df['Type 1']=='Fire','Legendary']=True


# these dont work in pycharm use jupyter notebooks here

df.loc[df['Total']>500, ['Generation','Legendary']]=['Test 1','Test 2']
