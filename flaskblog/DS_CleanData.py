import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Clean_data():
    df = pd.read_csv("train.csv")
    for column in df.columns:
        numNull = df[column].isnull().sum()
        twntypercnt = (df.shape[0]* 0.20)
        if numNull > twntypercnt:
            df=df.drop(column, axis = 1)
            continue
    return df


firstOption= input("type only one: PassengerId or Survived: ")
secondOption = input("Type ony one from: Sex or Age: ")
print(Clean_data())