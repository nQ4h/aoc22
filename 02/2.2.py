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
    if (input[i] == 'A'):           # Rock
        if(input[i+1] == 'X'):      # Lose
            score += 0
            score += 3
        elif(input[i+1] == 'Y'):    # Draw
            score += 3
            score += 1
        elif(input[i+1] == 'Z'):    # Win
            score += 6
            score += 2

    elif (input[i] == 'B'):         # Paper
        if(input[i+1] == 'X'):      # Lose
            score += 0
            score += 1
        elif(input[i+1] == 'Y'):    # Draw
            score += 3
            score += 2
        elif(input[i+1] == 'Z'):    # Win
            score += 6
            score += 3

    elif (input[i] == 'C'):         # Scissor
        if(input[i+1] == 'X'):      # Lose
            score += 0
            score += 2
        elif(input[i+1] == 'Y'):    # Draw
            score += 3
            score += 3
        elif(input[i+1] == 'Z'):    # Win
            score += 6
            score += 1

print (score)
'''
Rock = A, 1
Paper = B, 2
Scissors = C, 3

X lose, 0
Y draw , 3
Z  win, 6

'''