
#%%
## pandasを使って収集したデータについて軽く調べてみます。
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv( 'player_stats.csv' ,index_col=0)
data.head()


#%%
data.describe()


#%%
dan_carter = data.query('Pts == 1598')
dan_carter.head()


#%%
points = data['Pts']
matches = data['Mat']

plt.scatter(matches,points)


#%%
result = data.query('Pts > 400')
result.head()


#%%
points = data['Pts']
positions = data['Position']

plt.scatter(points,positions)


#%%
dan_carter = data.query('Tries > 30')
dan_carter.head()


#%%
temp_data = []
for span in data.Span:
    texts = span.split("-")
    temp_data.append(int(texts[1]) - int(texts[0]) + 1)

print(temp_data)
data["SpanYear"] = temp_data


#%%
data.head()


#%%
dan_carter = data.query('Tries > 30')
dan_carter.head()


