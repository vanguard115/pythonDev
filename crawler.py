
import urllib.parse, urllib.error, urllib.request
from bs4 import BeautifulSoup

url = input("Enter the url:- ")

html = urllib.request.urlopen(url).read()
# print('# DEBUG: ',html)

soup = BeautifulSoup(html, 'html.parser')

# print('# DEBUG: ',soup)

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
