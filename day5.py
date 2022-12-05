import sys


def readText(filename):

    data = open(filename, 'r')
    for line in data.readlines():
        if line[0] != '\n':
            print()
        else:
            continue
    print("The answer for the first part is: ", )
    print("The answer for the second part is: ", )


if len(sys.argv) == 2:
   lines = readText(sys.argv[1])
else:
    print("No Input File Supplied")