
#%%
import urllib.request
import bs4
import pandas as pd

path = "players_link.txt"

with open(path) as f:
    links = f.readlines()
    
data_frame = pd.DataFrame()
    
for index, link in enumerate(links):
    link = link.replace('\n','')
    url = 'http://en.espn.co.uk/' + link
    soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")

    print(str(index) + ":" + link)

    data = soup.find("div", class_="scrumPlayerName")

    stats = {}
    stats["name"] = data.string

    data = soup.find_all("div", class_="scrumPlayerDesc")
    for item in data:
        try:
            key = item.find("b").string
            text = str(item)
            start_index = text.find("</b>")
            end_index = text.find("</div>")
            value = text[start_index + 4:end_index].strip()
            stats[key] = value
        except AttributeError:
            pass

    data = soup.find("thead").find_all("th")
    head =[]
    for item in data:
        head.append(item.string)


    data = soup.find("table", class_="engineTable").find_all("tr")
    for item in data:
        if item.find("b").string == "All Tests":
            for index, table_data in enumerate(item.find_all("td")):
                if index > 0:
                    stats[head[index]] =  table_data.string
                    
    for column in stats.keys():
        if not column in data_frame.columns:
            data_frame[column] = 0               
        
    values = []
    for v in stats.values():
        values.append(v)

        
    series = pd.Series(values, index=stats.keys())
    data_frame = data_frame.append(series, ignore_index = True)
    


#%%
data_frame.head()


#%%
data_frame.describe()


#%%
data_frame.to_csv( 'player_stats.csv' )


