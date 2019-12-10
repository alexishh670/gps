import requests
import bs4

response = requests.get ('http://gpsui.net/u/vZKm')

#print(response.text)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
x=soup.find("meta", {"itemprop":"image"})
print(x)

# for m in meta.find_all('content'):
#     print(m['content'])

#print(soup.meta['content'][1])