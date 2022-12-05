import sys


def readText(filename):
    play_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

    data = open(filename, 'r')
    plays = []

    score = 0
    score2 = 0

    for line in data.readlines():
        if line[0] != '\n':
            foe, me = (str(x) for x in line.split())
            plays.append([play_dict[foe], play_dict[me]])
        else:
            continue

    for j, i in plays:
        if i == j:
            score += i + 3
        elif (i == 1 and j == 3) or (i == 3 and j == 2) or (i == 2 and j == 1):
            score += i + 6
        else:
            score += i
    print("Puzzle 1 : ", score)

    # Rock = A(1) | Paper = B(2) | Scissors = C(3)
    for j, i in plays:
        if i == 1:  # Lose
            if j == 1:
                score2 += 3
            if j == 2:
                score2 += 1
            if j == 3:
                score2 += 2
        elif i == 2:  # Draw
            score2 += j + 3
        else:  # Win
            if j == 1:
                score2 += 2 + 6
            if j == 2:
                score2 += 3 + 6
            if j == 3:
                score2 += 1 + 6
    print("Puzzle 2 : ", score2)

if len(sys.argv) == 2:
   lines = readText(sys.argv[1])
else:
    print("No Input File Supplied")
