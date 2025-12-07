sum = 0
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
l = len(lines)
w = 0
for i in lines:
    w = max(w, len(i))
grid = []
for i in lines:
    grid.append(i.ljust(w))
start = 0
for j in range(w + 1):
    empty = True
    if j < w:
        for i in range(l):
            if grid[i][j] != ' ':
                empty = False
                break
    if empty:
        if j > start:
            nums = []
            op = ''
            sub = []
            for i in range(l):
                sub.append(grid[i][start:j])
            op = sub[-1].strip()
            for i in range(l - 1):
                n = sub[i].strip()
                if n:
                    nums.append(int(n))
            if op == '+':
                res = 0
                for n in nums:
                    res += n
                sum += res
            elif op == '*':
                res = 1
                for n in nums:
                    res *= n
                sum += res
        start = j + 1
print('answer is', sum)