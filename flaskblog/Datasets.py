import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from pandasql import sqldf

pysqldf = lambda q: sqldf(q, globals())

df = pd.read_csv('train.csv')
print(df)
dfs = df[0:10]
print(dfs)

avgAge = df.Age.mean()
avgFare= df.Fare.mean()
male = df['Sex'].value_counts().male
female = df['Sex'].value_counts().female
all =df.Sex.count()
maleCount=((male/all)*100).round(0)
femaleCount= 100-maleCount

print(avgAge)
print(avgFare)
print(maleCount)
print(femaleCount)

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



#df = pd.DataFrame({'items':['Age', 'Fare', 'male (%)', 'female (%)'], 'val':[avgAge, avgFare, maleCount, femaleCount]})
#ax = df.plot.bar(x='items', y='val', rot=0)

#plt.show()#