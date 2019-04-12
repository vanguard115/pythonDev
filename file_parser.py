
yes_loop = 'Y'
while yes_loop=='Y' or yes_loop == 'y':
    fileName = input("Which file do you wish to count? ")
    try:
        fileHandle = open(fileName)

        count = 0
        for line in fileHandle:
            if line.startswith("Subject:"):
                count = count + 1
        print("The file",fileName,"contains",count,"lines that start with Subject")
        yes_loop=input("Wish to continue [Y/N]")

    except:
        print("The mentioned file cannot be found, enter a valid name")
        yes_loop=input("Wish to continue [Y/N]")
