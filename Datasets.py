import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandasql import sqldf


pysqldf = lambda q: sqldf(q, globals())

sns.set_theme(style='darkgrid')

df = pd.read_csv('train.csv')

#print(df)

dfs = df[1:5]

print(dfs)

q = """SELECT Age 
       FROM df 
       LIMIT 10;"""

names = pysqldf(q)
print(names)
