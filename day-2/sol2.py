sum = 0
def check(n):
    num = str(n)
    l = len(num)
    for parts in range(2, l + 1):
        if l % parts == 0:
            size = l // parts
            if num[:size] * parts == num:
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