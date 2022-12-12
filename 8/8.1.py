map = open("8.txt", "r").read().splitlines()
seen = []
nRows = len(map)

for i in range(nRows):
    str = [0]
    for i in range(len(map[i])-1):
        str.append(0)
    seen.append(str)

def findHorizontal(jStart, jEnd, jIncrement):
    trees = 0
    for i in range(nRows):
        max = -1
        for j in range(jStart, jEnd, jIncrement):
            if(int(map[i][j])>int(max)):
                max = map[i][j]
                if(not int(seen[i][j])):
                    trees += 1
                    seen[i][j] = 1
    return trees

def findVertical(iStart, iEnd, iIncrement):
    trees = 0
    for j in range(nRows):
        max = -1
        for i in range(iStart, iEnd, iIncrement):
            if(int(map[i][j])>int(max)):
                max = map[i][j]
                if(not int(seen[i][j])):
                    trees += 1
                    seen[i][j] = 1
    return trees

def main():
    print(findHorizontal(0, nRows, 1) + findHorizontal(nRows-1, -1, -1) + findVertical(0, nRows, 1) + findVertical(nRows-1, -1, -1))

if __name__ == "__main__":
    main()