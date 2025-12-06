ctr = 0
ranges = []
mode = "ranges"

with open("input.txt", "r") as file:
    content = file.read().splitlines()
    
    for line in content:
        if line == "":
            mode = "check"
            continue
            
        if mode == "ranges":
            parts = line.split('-')
            start = int(parts[0])
            end = int(parts[1])
            ranges.append((start, end))
                
        elif mode == "check":
            val = int(line)
            found = False
            for r in ranges:
                if r[0] <= val <= r[1]:
                    found = True
                    break
            if found:
                ctr += 1

print('answer is', ctr)