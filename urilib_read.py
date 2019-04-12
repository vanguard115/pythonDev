import urllib.parse, urllib.request, urllib.error
import re

fileHandel = urllib.request.urlopen('http://192.168.26.123/')
urlList = []
for line in fileHandel:
    urls = re.findall('href="http[s]?://.+?"',line.decode())
    # print(line.decode())
    if len(urls)<1:continue
    print('# DEBUG: ',urls)
    urlList.append(urls)

print(urlList)
