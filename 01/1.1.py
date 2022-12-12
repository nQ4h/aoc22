value = 0
bigValue = 0

with open(r"/home/noah/aoc22/1.txt", 'r') as fp:
    nLines = len(fp.readlines())

for i in range(nLines):
    temp = input()
    if (temp != ""):
        temp = int(temp)
        value = temp + value
    else:
        if(value > bigValue):
            bigValue = value
        value = 0
        
print(bigValue)