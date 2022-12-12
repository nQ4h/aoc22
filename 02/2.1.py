import re
with open(r"/home/noah/aoc22/2.txt", 'r') as fp:
    input = fp.read()
input = re.sub(r'\s+', '', input)

with open(r"/home/noah/aoc22/2.txt", 'r') as fp:
    nLines = len(fp.readlines())

print(input)
print(nLines)
score = 0
for i in range(0, nLines*2, 2):
    print (input[i+1])


for i in range(0, nLines*2, 2):
    if (input[i] == 'A'):
        if(input[i+1] == 'X'):
            score += 1
            score += 3
        elif(input[i+1] == 'Y'):
            score += 2
            score += 6
        elif(input[i+1] == 'Z'):
            score += 3
            score += 0

    elif (input[i] == 'B'):
        if(input[i+1] == 'X'):
            score += 1
            score += 0
        elif(input[i+1] == 'Y'):
            score += 2
            score += 3
        elif(input[i+1] == 'Z'):
            score += 3
            score += 6 

    elif (input[i] == 'C'):
        if(input[i+1] == 'X'):
            score += 1
            score += 6
        elif(input[i+1] == 'Y'):
            score += 2
            score += 0
        elif(input[i+1] == 'Z'):
            score += 3
            score += 3

print (score)
'''
Rock = A , X
Paper = B, Y
Scissors = C, Z
(1 for Rock, 2 for Paper, and 3 for Scissors) 
(0 if you lost, 3 if the round was a draw, and 6 if you won).
'''