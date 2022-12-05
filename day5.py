import sys


def readText(filename):
    total = 0
    total2 = 0
    data = open(filename, 'r')
    for line in data.readlines():
        if line[0] != '\n':
                else:
            continue
    print("The answer for the first part is: ", total)
    print("The answer for the second part is: ", total + total2)


if len(sys.argv) == 2:
   lines = readText(sys.argv[1])
else:
    print("No Input File Supplied")