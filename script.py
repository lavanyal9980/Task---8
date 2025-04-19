import pandas as pd 
import numpy as np

df = pd.read_csv(r'C:\Users\Lavanya\Downloads\archive\Sample - Superstore.csv', encoding='ISO-8859-1')


print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df.duplicated())

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')

df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
