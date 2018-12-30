
#%%
## pandasを使って収集したデータについて軽く調べてみます。
import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt

data = pd.read_csv( 'player_world_stats.csv' ,index_col=0)
print(data.columns)
data = data[['name', 'Born','Span','Position','Mat','Start','Sub','Pts','Tries','Conv','Pens','Drop','%','Height','Weight']]

temp_span_year = []
temp_span_start = []
for span in data.Span:
    texts = span.split("-")
    temp_span_year.append(int(texts[1]) - int(texts[0]) + 1)
    temp_span_start.append(int(texts[0]))

data["Span"] = temp_span_year
data["SpanStart"] = temp_span_start

temp_born = []
for born in data.Born:
    result = re.search('1\d{3}', str(born))
    if result == None:
        temp_born.append(0)
    else:
        temp_born.append(int(result.group()))

data["Born"] = temp_born

data.head()

#%%
temp_weight = []
for weight in data.Weight:
    result = str(weight).replace(' lb','')
    temp_weight.append(0.45359237 * float(result))

data["Weight"] = temp_weight

temp_height = []

for height in data.Height:
    texts = str(height).split(" ")
    height_data = 0
    if len(texts) >= 3:        
        height_data = (float(texts[0]) * 12 + float(texts[2])) * 2.54

    temp_height.append(height_data)

data["Height"] = temp_height
data.head()
#%%
data.describe()
#%%
result = data.query("Mat == 148")
result.head()


#%%
result = data.query("Sub == 55")
result.head()


#%%
result = data.query("Tries == 69")
result.head()


#%%
result = data.query("Won == 131")
result.head()


#%%
result = data.query("Lost == 100")
result.head()


#%%
points = data['Pts'] / data['Mat']
matches = data['Mat']

plt.scatter(matches,points)


#%%
data['Rate'] =  data['Pts'] / data['Mat']


#%%




result = data.query("Rate > 10 & Span + SpanStart >= 2018 ") #data.query("Mat > 50 & Rate > 8 & Span + SpanStart >= 2018 ")
result.tail()


#%%
result = data.query("Conv == 293 & Pens == 281")
result.head()


#%%
result = data.query("Drop == 36")
result.head()




#%%
result = data.query("Height > 200 ")
result.head()

#%%
x = data['Height']
y = data['Weight']

plt.xlim(150,200)
plt.ylim(50,200)
plt.scatter(x,y)
plt.show()


#%%
points = data['Height']
positions = data['name']

plt.scatter(points,positions)


#%%
