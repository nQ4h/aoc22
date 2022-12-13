import heapq
lines = open("11.txt", "r").read().splitlines()
monkeys = []
for i in range(len(lines)):
    if(lines[i].__contains__("Starting items:")):
        items = lines[i].split(":")[-1]
        items = items.split(", ")
        monkeys.append(items)
times = [0] * 8
mgm = 11*3*5*7*19*2*13*17
for z in range(10000):
    for i in range(len(monkeys)):
        x = len(monkeys[i])
        for j in range(x):
            temp = int(monkeys[i][0])
            monkeys[i].remove(monkeys[i][0])
            times[i] += 1
            if (i == 0):
                temp = (temp*17)%mgm
                if(temp%11 == 0):
                    monkeys[2].append(temp)
                else:
                    monkeys[3].append(temp)
            if (i == 1):
                temp = (temp+7)%mgm
                if(temp%3 == 0):
                    monkeys[6].append(temp)
                else:
                    monkeys[5].append(temp)
            if (i == 2):
                temp = (temp*temp)%mgm
                if(temp%5 == 0):
                    monkeys[1].append(temp)
                else:
                    monkeys[7].append(temp)
            if (i == 3):
                temp = (temp+1)%mgm
                if(temp%7 == 0):
                    monkeys[2].append(temp)
                else:
                    monkeys[7].append(temp)
            if (i == 4):
                temp = (temp*3)%mgm
                if(temp%19 == 0):
                    monkeys[0].append(temp)
                else:
                    monkeys[3].append(temp)
            if (i == 5):
                temp = (temp+4)%mgm
                if(temp%2 == 0):
                    monkeys[6].append(temp)
                else:
                    monkeys[4].append(temp)
            if (i == 6):
                temp =(temp+8)%mgm
                if(temp%13 == 0):
                    monkeys[4].append(temp)
                else:
                    monkeys[0].append(temp)
            if (i == 7):
                temp =(temp+6)%mgm
                if(temp%17 == 0):
                    monkeys[1].append(temp)
                else:
                    monkeys[5].append(temp)
_max = heapq.nlargest(2, range(len(times)), key=times.__getitem__)
print(times[_max[0]] * times[_max[1]])