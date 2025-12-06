ctr = 0
grid = []
with open("input.txt", "r") as file:
    content = file.read()
    grid = content.splitlines()

rows = len(grid)
cols = len(grid[0])
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '@':
            adj = 0
            for k in range(8):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == '@':
                        adj += 1
            if adj < 4:
                ctr += 1
print('answer is', ctr)