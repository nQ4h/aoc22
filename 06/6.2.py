string = input()
found = index = 0
while(not found):
    list = []
    for i in range(index, index+14):
        list.append(string[i])
    _set = set(list)
    if(len(list) == len(_set)):
        print(index+14)
        found = 1
    else:
        index+=1