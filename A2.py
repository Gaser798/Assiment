import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


result = requests.get('https://myanimelist.net/topanime.php?type=airing')

src = (result.content)

soap = BeautifulSoup(src, 'lxml')

Anime = soap.find_all('a', {'class': 'hoverinfo_trigger fl-l ml12 mr8'})

Anime_name =[]

for i in Anime:
    Anime_name.append(i.findNext('a').text)


name =[Anime_name]

exp = zip_longest(*name)


with open('data.csv','w',encoding='utf-8')as f:
    f = csv.writer(f)
    f.writerow(['Anime Name'])
    f.writerows(exp)