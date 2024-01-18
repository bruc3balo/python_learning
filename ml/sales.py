import pandas as pd
dataframe = pd.read_csv('/Users/bruc3balo/Downloads/jupyter/vgsales.csv')

#PRINT DATAFRAME
print(dataframe)

#Print ANALYSISS
print(dataframe.describe())

#Print values
print(dataframe.values)

#Create dataset with new names
x = dataframe.drop(columns=['Other_Sales'])
print(x)

#Access column
years = dataframe['Year']
print(years)