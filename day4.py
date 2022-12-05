import sys


def readText(filename):
    total = 0
    total2 = 0
    data = open(filename, 'r')
    for line in data:
        if line[0] != '\n':
            pair1, pair2 = line.split(',')
            a, b = pair1.split('-')
            c, d = pair2.split('-')
            a, b, c, d = int(a), int(b), int(c), int(d)
            result1 = list(range(a, b + 1))
            result2 = list(range(c, d + 1))
            if all(value in result1 for value in result2):
                total += 1
            elif all(value in result2 for value in result1):
                total += 1
            if any(value in result1 for value in result2):
                total2 += 1
        else:
            continue
    print("The answer for the first part is: ", total)
    print("The answer for the second part is: ", total2)


if len(sys.argv) == 2:
   lines = readText(sys.argv[1])
else:
    print("No Input File Supplied")