from collections import defaultdict

curr = defaultdict(int)
grid = []
with open("input.txt", "r") as file:
    grid = file.read().splitlines()

rows = len(grid)
cols = len(grid[0])
startRow = 0

for i in range(rows):
    if 'S' in grid[i]:
        curr[grid[i].index('S')] = 1
        startRow = i
        break

for i in range(startRow + 1, rows):
    nextBeams = defaultdict(int)
    for col, count in curr.items():
        if 0 <= col < cols:
            if grid[i][col] == '^':
                nextBeams[col - 1] += count
                nextBeams[col + 1] += count
            else:
                nextBeams[col] += count
        else:
            nextBeams[col] += count
    curr = nextBeams

print('answer is', sum(curr.values()))