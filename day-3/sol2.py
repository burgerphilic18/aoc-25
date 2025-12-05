sum = 0
with open("input.txt", "r") as file:
    content = file.read()
    contentList = content.splitlines()
    for i in contentList:
        curr = 0
        num = ''
        for j in range(12):
            rem = 11 - j
            limit = len(i) - rem
            sub = i[curr:limit]
            best = max(sub)
            num += best
            curr += sub.index(best) + 1
        sum += int(num)
    print('answer is', sum)