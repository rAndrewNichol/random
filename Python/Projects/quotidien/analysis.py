import daily_retrieval as sql
import pandas as pd
import numpy as np
import re
import os

os.chdir('C:/Users/Andrew/Documents/Coding/PythonFiles/Projects/quotidien')

df = sql.retrieve_dataframe(p = 'rezzonico', db = 'spring2017')
print(df.columns.values)
print(df.head())

# print(np.mean(df['cs_study']))
# print(type(df['sleep'][0]))
# print(df['sleep'][:])
# print(len(df['sleep'][:]))

# expects list 'times'
# def convert_times(times):
# 	for x in times:

df.to_csv('data.csv')

