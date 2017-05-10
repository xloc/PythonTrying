import numpy as np
data = np.zeros(shape=(11, 67))

with open('data.txt') as f:
    for line in f.readlines():
        numbers = map(int, (line[0:2], line[2:4], line[4:5]))
        row, col = numbers[0:2]
        val = numbers[2]

        data[row][col] = val
