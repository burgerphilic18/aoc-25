import math

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
components = l

def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]

ans = 0
for d, u, v in dists:
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        parent[root_u] = root_v
        components -= 1
        if components == 1:
            ans = arr[u][0] * arr[v][0]
            break

print('answer is', ans)