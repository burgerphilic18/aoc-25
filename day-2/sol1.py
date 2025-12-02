sum = 0
def check(n):
    num = str(n)
    l = len(num)
    if l % 2 != 0:
        return False
    half = l // 2
    if num[:half] == num[half:]:
        return True
    return False
with open("input.txt", "r") as file:
    ID = file.read().strip()
    IDList = ID.split(',')
    for i in IDList:
        IDpair = i.split('-')
        for j in range(int(IDpair[0]), int(IDpair[1]) + 1):
            if check(j):
                sum += j
    print('answer is', sum)