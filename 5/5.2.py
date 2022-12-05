with open("5.txt", 'r') as fp:
    nLines = len(fp.readlines())

stack1 = ['B','L','D','T','W','C','F','M']
stack2 = ['N','B','L']
stack3 = ['J','C','H','T','L','V']
stack4 = ['S','P','J','W']
stack5 = ['Z','S','C','F','T','L','R']
stack6 = ['W','D','G','B','H','N','Z']
stack7 = ['F','M','S','P','V','G','C','N']
stack8 = ['W','Q','R','J','F','V','C','Z']
stack9 = ['R','P','M','L','H']
stackList = [0,stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]

tempList = list()
for i in range(nLines):
    str = input()
    list = str.split(" ")
    temp1 = stackList[int(list[3])]
    temp2 = stackList[int(list[5])]
    for x in range(int(list[1])):
        tempList.append(temp1.pop())
    for x in range(int(list[1])):
        temp2.append(tempList.pop())
for x in range(1,10):
    temp = stackList[x]
    print(temp[-1], end="")
print("")