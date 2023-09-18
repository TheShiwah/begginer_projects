import requests
from bs4 import BeautifulSoup

url = 'https://www.eplstreams.xyz'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h5', {'class': 'post-title'})
title1 = title[0].getText()
print(title)

'''for t in title: 
    print(t.getText())'''



