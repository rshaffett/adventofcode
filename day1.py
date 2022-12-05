import heapq
import sys

def readText(filename):
    calories = 0

    data = open(filename, 'r')
    elfcals = []

    for line in data.readlines():
        if line[0] != '\n':
            calories += int(line)
        else:
            elfcals.append(calories)
            calories = 0
            continue
    elfcals.append(calories)

    print("Highest Calories Carried : ", max(elfcals))
    print("Sum of Top 3 Calories Carried : ", sum(heapq.nlargest(3, elfcals)))


if len(sys.argv) == 2:
   lines = readText(sys.argv[1])
else:
    print("No Input File Supplied")
