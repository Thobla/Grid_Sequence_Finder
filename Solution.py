from enum import Enum
import csv
data = [
    [23, 34, 55, 43, 84, 32],
    [33, 11, 55, 53, 43, 50],
    [33, 24, 54, 22, 43, 146],
    [33, 11, 55, 53, 103, 10]
]

##########  PART 1 ######################
# Convert to csv file
with open ("csv_file.csv", mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerows(data)

##########  PART 2 #######################
class Direction(Enum):
    RIGHT = 1
    DOWNRIGHT = 2
    DOWN = 3
    DOWNLEFT = 4


seq_len = 3

# Read sequence
def add_next(x, y, grid, dir, sequence, num=seq_len):
    if num == 0
        return sequence
    sequence.append(grid[y][x])

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
seq = data[0][:seq_len]
max_val = sum(seq)

# Find highest sequence
for x in range(len(data[0])):
    for y in range(len(data)):
        for temp_dir in Direction:
            new_seq = add_next(x, y, data, temp_dir, sequence=[])
            if sum(new_seq) >= max_val:
                max_val = sum(new_seq)
                seq = new_seq
                dir = temp_dir
                pos = (x, y)


# Print answer
print("sum = ", max_val)
print("sequence = ", seq)
print("grid position = ", pos)
print("direction = ", dir)
