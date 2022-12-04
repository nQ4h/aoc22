with open("4.txt", 'r') as fp:
    nLines = len(fp.readlines())
n = 0
for i in range(nLines):
    str = input()
    list = str.split(',')
    range1 = list[0].split('-')
    range2 = list[1].split('-')
    num1 = int(range1[0])
    num2 = int(range1[1])
    num3 = int(range2[0])
    num4 = int(range2[1])
    if(num1 >= num3 and num1 <= num4):
        n+=1
        continue
    if(num2 >= num3 and num2 <= num4):
        n+=1
        continue
    if(num3 >= num1 and num3 <= num2):
        n+=1
        continue
print(n)