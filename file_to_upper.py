

try:
    fhandle = open('mbox.txt')
except:
    print("The file does not exixts")

count=0
for line in fhandle:
    print(line.upper())
    count=count+1
    if count >= 10:
        exit()
