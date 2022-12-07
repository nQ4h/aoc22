string = input()
ok = 0
for i in range(len(string)):
    if (ok == 4):
        print(i)
        break
    if(string[i] != string[i+1] and string[i] != string[i+2] and string[i] != string[i+3]):
        ok += 1
    else:
        ok = 0