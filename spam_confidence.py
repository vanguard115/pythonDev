
fileName  = input("Enetr the file you need to check ")
if fileName == "na na boo boo":
    print("NA NA BOO BOO TO YOU TOO - Yee Have been a punk'd!!")
    exit()

count=0
spamSum=0
try:
    fileHandle = open(fileName)
except:
    print("Sorry the file does not exist")
    exit()

for line in fileHandle:
    if line.startswith("X-DSPAM-Confidence:"):
        spamValue = float(line[20:])
        count = count + 1
        spamSum = spamSum + spamValue

print(count,spamSum/count)
