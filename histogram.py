
try:
    fileHandel = open('mbox.txt')
except:
    print("File not found")
    exit()

histo = dict()
words = []
for line in fileHandel:
    if len(line.strip())!=0:
        line.rstrip()
        words = line.split()
        # print('Debug:',words)
        if words[0]=='From':
            word = words[1]
            if histo.get(word,0) == 0:
                histo[word] = 1
            else:
                histo[word] +=1
    else:
        continue

# for x in histo:
#     print(x,histo[x])

all_stuff  = list(histo.keys())
# print(all_stuff)
# print(all_stuff[1])


low = all_stuff[0]
high = all_stuff[0]
# print(high,low)
# highest = histo[0]
# lowest = histo[0]
for x in histo:
    # print("Debug:",x)
    if histo[x] > histo[high]:
        high = x
        # print("Debug:",x,histo[high],histo[low])
    if histo[x] < histo[low]:
         low = x
    else:
        continue

print(high,histo[high],low,histo[low])
