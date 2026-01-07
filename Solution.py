from enum import Enum
import csv
import math

grid = []
with open("grid3.txt") as f:
    for line in f:
        grid.append([int(x) for x in line.strip().split()]) # write to array

##########  PART 1 ######################
# Convert to csv file
with open ("csv_file.csv", mode='w', newline='') as f:
    writer = csv.writer(f)

    writer.writerows(grid)

##########  PART 2 #######################
class Direction(Enum):
    RIGHT = 1
    DOWNRIGHT = 2
    DOWN = 3
    DOWNLEFT = 4


seq_len = 4

# Read sequence
def add_next(x, y, grid, dir, sequence, num=seq_len):
    if num == 0:
        return sequence
    sequence[0].append(grid[y][x])
    sequence[1].append((x, y))

    if dir == Direction.RIGHT:
        x += 1
    elif dir == Direction.DOWNRIGHT:
        x += 1
        y += 1
    elif dir == Direction.DOWN:
        y += 1
    elif dir == Direction.DOWNLEFT:
        x -= 1
        y += 1

    if not(0 <= x < len(grid[0])) or not(0 <= y < len(grid)):
        return sequence

    return add_next(x, y, grid, dir, sequence=sequence, num=num-1)


# Innitialize answer
pos = (0, 0)
dir = Direction.RIGHT # make 
seq = grid[0][:seq_len]
indecies = [(0, y) for y in range(seq_len)]
max_val = math.prod(seq)

# Find highest sequence
for x in range(len(grid[0])):
    for y in range(len(grid)):
        for temp_dir in Direction:
            new_seq, new_ind = add_next(x, y, grid, temp_dir, sequence=([],[]))
            if math.prod(new_seq) >= max_val:
                max_val = math.prod(new_seq)
                seq = new_seq
                indecies = new_ind
                dir = temp_dir
                pos = (x, y)

# Print answer
print("grid start position = ", pos)
print("direction = ", dir)
print("sequence = ", seq)
print("indecies = ", indecies)
print("prod = ", max_val)