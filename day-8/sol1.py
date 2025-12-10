import math
from collections import defaultdict

arr = []
with open("input.txt", "r") as file:
    content = file.read().splitlines()
    for i in content:
        p = i.split(',')
        arr.append((int(p[0]), int(p[1]), int(p[2])))

dists = []
l = len(arr)
for i in range(l):
    for j in range(i + 1, l):
        d = math.sqrt((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2 + (arr[i][2] - arr[j][2])**2)
        dists.append((d, i, j))

dists.sort()

parent = list(range(l))

def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]

for k in range(1000):
    if k < len(dists):
        d, u, v = dists[k]
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_u] = root_v

sizes = defaultdict(int)
for i in range(l):
    root = find(i)
    sizes[root] += 1

vals = sorted(sizes.values(), reverse=True)
ans = 1
for i in range(3):
    if i < len(vals):
        ans *= vals[i]

print('answer is', ans)