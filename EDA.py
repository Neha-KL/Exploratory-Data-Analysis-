import pandas as pd
import numpy as np 

#read the file
df = pd.read_csv("D:\data\Amazon Sales Dataset.csv")

#Basic info
print(df.info())
print(df.describe())
print(df.head())

#Data cleaning and handling missing value 
print(df.isnull().sum())

df.fillna(df.mean(), inplace=True)  # Fill numerical columns with mean
#df.dropna(inplace=True)

print(df.isnull().sum())