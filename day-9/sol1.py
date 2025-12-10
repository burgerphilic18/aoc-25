ans = 0
arr = []
with open("input.txt", "r") as file:
    content = file.read().splitlines()
    for i in content:
        p = i.split(',')
        arr.append((int(p[0]), int(p[1])))

l = len(arr)
for i in range(l):
    for j in range(i + 1, l):
        w = abs(arr[i][0] - arr[j][0]) + 1
        h = abs(arr[i][1] - arr[j][1]) + 1
        area = w * h
        if area > ans:
            ans = area

print('answer is', ans)