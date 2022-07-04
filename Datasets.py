import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandasql import sqldf


pysqldf = lambda q: sqldf(q, globals())

sns.set_theme(style='darkgrid')

df = pd.read_csv('train.csv')

print(df)

dfs = df[0:10]

print(dfs)

q = """SELECT AVG(Age) 
       FROM df;
       """

avgAge = pysqldf(q)

q = """SELECT AVG(Fare)
        FROM df;
        """
avgFare = pysqldf(q)

q = """SELECT COUNT(Sex)
        FROM df
        WHERE Sex = 'male';
        """
maleCount = pysqldf(q)

q = """SELECT COUNT(Sex)
        FROM df
        WHERE Sex = 'female';
        """
femaleCount = pysqldf(q)

print(avgAge)
print(avgFare)
print(maleCount)
print(femaleCount)
print()
print(pd.isnull(df.Age[5]))

df = pd.DataFrame({'lab':['Age', 'Fare', 'male', 'female'], 'val':[avgAge, avgFare, maleCount, femaleCount]})
ax = df.plot.bar(x='lab', y='val', rot=0)

plt.show()