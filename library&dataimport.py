#need to install: python -m pip install plotly
import plotly.express as px
import pandas as pd

df = pd.read_csv('train.csv')
df.head()
#df.columns
#df.WELL.unique()
#select subset of the data
#df_well = df[df['WELL']=='15/9-13']# not sure what this does
#df_well


