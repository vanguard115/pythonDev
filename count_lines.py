
fhand = open('mbox.txt')
# readHand = fhand.read()

# print(readHand)

for line in fhand:
    if line.startswith('From:'):
        line = line.strip()
        print(line)
# readHand
