
import re
try:
    fileName = input("Enter the file name ")
    fileHandel = open(fileName)
except:
    print("Nope, that file is not there")
    exit()


n=0
sum=0
#New Revision: 39772
for line in fileHandel:
    line.rstrip()
    x = re.findall('New Revision: ([0-9.].+)',line)
    if len(x)>0:
        sum = sum + int(x.pop())
        n +=1

print('Average = ',sum/n)
