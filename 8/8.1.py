with open("t.txt", 'r') as fp:
    nLines = len(fp.readlines())

map = []
seen = []
visibleTrees = 0
for i in range(nLines):
    map.append(input())

for i in range(nLines):
    str = [0]
    for i in range(len(map[i])-1):
        str.append(0)
    seen.append(str)

#i row, j column
#Check from left to right
print("Left to right:")
for i in range(0, nLines):
    for j in range(0, len(map[i])):
        if(int(map[i][j])<int(map[i][j+1])):
            if(not seen[i][j]):
                visibleTrees += 1
                seen[i][j] = 1
            print(map[i][j],"<", map[i][j+1], "\t-> visibleTrees = ", visibleTrees)
        else:
            if(not seen[i][j]):
                visibleTrees += 1
                seen[i][j] = 1
            print(map[i][j],">=", map[i][j+1], "\t-> visibleTrees = ", visibleTrees)
            break

#Check from right to left
print("Right to left:")
for i in range(0, nLines):
    for j in range(len(map[i])-1, 0, -1):
        if(int(map[i][j])<int(map[i][j-1])):
            if(not seen[i][j]):
                visibleTrees += 1
                seen[i][j] = 1
            print(map[i][j],"<", map[i][j-1], "\t-> visibleTrees = ", visibleTrees)
        else:
            if(not seen[i][j]):
                visibleTrees += 1
                seen[i][j] = 1
            print(map[i][j],">=", map[i][j-1], "\t-> visibleTrees = ", visibleTrees)
            break

#Check from top to bottom
print("Top to bottom:")
for j in range(0, len(map[i])):
    for i in range(0,nLines-1):
        if(int(map[i][j]) < int(map[i+1][j])):
            if(not seen[i][j]):
                visibleTrees += 1
                seen[i][j] = 1
            print(map[i][j],"<", map[i+1][j], "\t-> visibleTrees = ", visibleTrees)
        else:
            if(not seen[i][j]):
                visibleTrees += 1
                seen[i][j] = 1
            print(map[i][j],">=", map[i+1][j], "\t-> visibleTrees = ", visibleTrees)
            break

#Check from bottom to top
print("Bottom to top:")
for j in range(0, len(map[i])):
    for i in range(nLines-1, 0, -1):
        if(int(map[i][j]) < int(map[i-1][j])):
            if(not seen[i][j]):
                visibleTrees += 1
                seen[i][j] = 1
            print(map[i][j],"<", map[i-1][j], "\t-> visibleTrees = ", visibleTrees)
        else:
            if(not seen[i][j]):
                visibleTrees += 1
                seen[i][j] = 1
            print(map[i][j],">=", map[i-1][j], "\t-> visibleTrees = ", visibleTrees)
            break

for i in range(nLines):
    print(map[i])

for i in range(nLines):
    print(seen[i])