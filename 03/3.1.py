import string
letters = string.ascii_letters

def valueOfChar(char):
    valueOfChar = 1
    for i in range(len(letters)):
        if (letters[i] == char):
            return valueOfChar
        valueOfChar += 1
    return valueOfChar

def findEqualChar(firstpart, secondpart):
    for char in firstpart:
        if char in secondpart:
            return valueOfChar(char)
    return 0

def main():
    sum = 0

    with open(r"/home/noah/aoc22/3.txt", 'r') as fp:
        nLines = len(fp.readlines())

    for i in range(nLines):
        string = input()
        firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
        sum += findEqualChar(firstpart, secondpart)
    
    print(sum)

if __name__ == "__main__":
    main()