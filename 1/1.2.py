value = 0
bigValue = [0,0,0]
sum = 0

with open(r"/home/noah/aoc22/1.txt", 'r') as fp:
    nLines = len(fp.readlines())

for i in range(nLines):
    temp = input()
    if (temp != ""):
        temp = int(temp)
        value = temp + value
    else:
        for x in range(3):
            if(value > bigValue[x]):
                bigValue[x] = value
                break
        value = 0
for x in range(3):
    sum += bigValue[x]
    
print(sum)