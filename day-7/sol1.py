ctr = 0
grid = []
with open("input.txt", "r") as file:
    grid = file.read().splitlines()
rows = len(grid)
cols = len(grid[0])
curr = set()
start_row = 0
for i in range(rows):
    if 'S' in grid[i]:
        curr.add(grid[i].index('S'))
        start_row = i
        break
for i in range(start_row + 1, rows):
    next_beams = set()
    for j in curr:
        if 0 <= j < cols:
            if grid[i][j] == '^':
                ctr += 1
                if j - 1 >= 0:
                    next_beams.add(j - 1)
                if j + 1 < cols:
                    next_beams.add(j + 1)
            else:
                next_beams.add(j)
    curr = next_beams
    if not curr:
        break
print('answer is', ctr)