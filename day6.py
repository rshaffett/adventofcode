import sys


def readText(filename):
    marker_length = 4
    count = marker_length - 1
    data = open(filename, 'r')
    for line in data:
        if line[0] != '\n':
            # Iterate over the string, starting from the first character
            for i in range(len(line) - marker_length + 1):
                # Get the current set of characters
                current_set = line[i:i+marker_length]
                count += 1

            # Check if the current set is unique
                if len(set(current_set)) == marker_length:
                    # If it is, print it and stop the loop
                    print("The answer to the first part is : ", count, '[', current_set, ']')
                    break

            marker_length = 14
            count = marker_length - 1
            for i in range(len(line) - marker_length + 1):
                # Get the current set of characters
                current_set = line[i:i+marker_length]
                count += 1

                if len(set(current_set)) == marker_length:
                    # If it is, print it and stop the loop
                    print("The answer to the second part is : ", count, '[', current_set, ']')
                    break

if len(sys.argv) == 2:
   lines = readText(sys.argv[1])
else:
    print("No Input File Supplied")