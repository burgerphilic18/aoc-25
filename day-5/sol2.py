ctr = 0
arr = []
with open("input.txt", "r") as file:
    content = file.read().splitlines()
    for i in content:
        if i == "":
            break
        p = i.split('-')
        arr.append((int(p[0]), int(p[1])))
arr.sort()
if arr:
    cs = arr[0][0]
    ce = arr[0][1]
    for i in range(1, len(arr)):
        s = arr[i][0]
        e = arr[i][1]
        if s <= ce:
            ce = max(ce, e)
        else:
            ctr += (ce - cs + 1)
            cs = s
            ce = e
    ctr += (ce - cs + 1)
print('answer is', ctr)