with open("4.txt", 'r') as fp:
    nLines = len(fp.readlines())
n = 0
for i in range(nLines):
    str = input()
    list = str.split(',')
    range1 = list[0].split('-')
    range2 = list[1].split('-')
    if(int(range1[0]) >= int(range2[0])):
        if(int(range1[1]) <= int(range2[1])):
            n+=1
            continue
    if(int(range2[0]) >= int(range1[0])):
        if(int(range2[1]) <= int(range1[1])):
            n+=1
print(n)