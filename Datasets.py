import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style='darkgrid')

df = pd.read_csv('train.csv')

sns.pairplot(
    df, hue='Survived')

plt.show()
