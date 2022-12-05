import sys
from string import ascii_letters


def readText(filename):
    total = 0
    total2 = 0
    p1, p2, p3 = 0, 1, 2
    list = []
    data = open(filename, 'r')
    for line in data.readlines():
        if line[0] != '\n':
            list.append(line.strip())
            firstcomp, secondcomp = line[:len(line)//2], line[len(line)//2:].strip()
            common = set(firstcomp).intersection(secondcomp)
            priority = "".join([str(ascii_letters.index(c) + 1) if c in ascii_letters else c for c in common])
            total += int(priority)
        else:
            continue
    print("The answer for the first part is", total)
    while p3 < len(list):
        bcommon = set(list[p1]).intersection(list[p2], list[p3])
        badge = "".join([str(ascii_letters.index(c) + 1) if c in ascii_letters else c for c in bcommon])
        total2 += int(badge)
        p1 += 3
        p2 += 3
        p3 += 3
    else:
        print("the answer for the second part is", total2)


if len(sys.argv) == 2:
   lines = readText(sys.argv[1])
else:
    print("No Input File Supplied")
