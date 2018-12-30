
#%%
import urllib.request
import bs4
# ESPNのニュージーランドの選手一覧ページにアクセスします。
url = 'http://en.espn.co.uk/newzealand/rugby/player/caps.html?team=8'
soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")
print(str(soup))


#%%
# 下記を参考にまずは、腕試し。
# https://qiita.com/Azunyan1111/items/9b3d16428d2bcc7c9406
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = bs4.BeautifulSoup(html, "html.parser")

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
title_tag = soup.title

# 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
title = title_tag.string

# タイトル要素を出力
print(title_tag)

# タイトルを文字列を出力
print(title)


#%%
# 手っ取り早く集めたいので、
# aタグを集める
# hrefの値がニュージーランドの選手のリンクか取得
# 配列に格納
# 配列を改行コードでjoinして保存

tags = soup.find_all("a")

path = "players_link.txt"
links = []

for tag in tags:
    href = tag.get("href")
    if href.find('/newzealand/rugby/player/') > -1:
        links.append(href)
        print(href)
        
with open(path, mode='w') as f:
    f.write('\n'.join(links))


