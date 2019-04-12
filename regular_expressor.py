
import re

try:
    fileName = input("Enter the file to be parsed ")
    fileHandel = open(fileName)
    regularExp = input("Enter the expression ")
except:
    print("Fine no existo")
    exit()

x= 0

for line in fileHandel:
     if re.findall(regularExp,line):
         x +=1
print("There are",x,"occurences of",regularExp)
