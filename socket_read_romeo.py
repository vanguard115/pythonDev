import socket
import re

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://192.168.26.123/ HTTP/1.0\r\n\r\n')
response = str()
urlList = []
while True:
    text = mysock.recv(1024)
    if len(text) < 1: break
    urls = re.findall('href="(http[s]?://.*?)"',text.decode())
    if len(urls)<1: continue
    # print('# DEBUG: ',urls)
    urlList.append(urls)

print(urlList)
