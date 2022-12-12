lines = open("10.txt", "r").read().splitlines()
x = 1
sum = 0
cycles = 0
for i in range(len(lines)):
    if (lines[i].startswith("noop")):
        cycles += 1
        if (cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220):
            sum += x*cycles
    else:
        for j in range(2):
            cycles += 1
            if (cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220):
                sum += x*cycles      
        temp = lines[i].split(" ")
        x += int(temp[1])
print(sum)