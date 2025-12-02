ctr = 50
ctr0 = 0
with open("input.txt", "r") as file:
    content = file.read()
    contentList = content.splitlines()
    for i in contentList:
        direction = i[0]
        number = int(i[1:])
        if direction == 'L':
            for j in range(number):
                ctr -= 1
                ctr = ctr % 100
                if ctr == 0:   
                    ctr0 += 1
        elif direction == 'R':
            for j in range(number):
                ctr += 1
                ctr = ctr % 100
                if ctr == 0:
                    ctr0 += 1
print('answer is', ctr0)