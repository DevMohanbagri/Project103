import pandas as pd
import plotly.express as px

df = pd.read_csv('data103.csv')
fig  = px.scatter(df, x = 'country', y = 'date', size = 'cases', color = 'country', size_max = 100)
fig.show()