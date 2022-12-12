import string
letters = string.ascii_letters

def valueOfChar(char):
    valueOfChar = 1
    for i in range(len(letters)):
        if (letters[i] == char):
            return valueOfChar
        valueOfChar += 1
    return valueOfChar

def findEqualChar(str1, str2, str3):
    for char in str1:
        if char in str2:
            for i in range(len(str3)):
                if (str3[i] == char):
                    return valueOfChar(char)
    return 0

def main():
    sum = 0

    with open(r"/home/noah/aoc22/3.txt", 'r') as fp:
        nLines = len(fp.readlines())
    nLines = int(nLines/3)
    for i in range(nLines):
        str1 = input()
        str2 = input()
        str3 = input()
        sum += findEqualChar(str1, str2, str3)
    
    print(sum)

if __name__ == "__main__":
    main()