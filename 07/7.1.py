def main():
    with open("7.txt", 'r') as fp:
        nLines = len(fp.readlines())
        currentDir = dirOrfile("root")
    
    nDirs = 0

    for i in range(nLines):
        command = input()

        if(command == "$ cd .."):
            print("cd ..")

            if(not currentDir.visited):
                currentDir.parentDir.size += currentDir.size
                currentDir.visited = 1

            currentDir = currentDir.parentDir
            print(currentDir.name, "size:", currentDir.size)

        elif(command.startswith("$ cd")):
            temp = dirOrfile(command.split(' ')[-1])
            print("cd", temp.name)

            if (temp.name in currentDir.subDirs):
                temp.parentDir = currentDir                
                currentDir = temp
                print(currentDir.name,"found")

            else:
                currentDir.subDirs.append(temp.name)
                temp.parentDir = currentDir
                currentDir = temp
                print("New subdir", currentDir.name)
                nDirs+=1

        elif (command == "$ ls"):
            print("ls")

        elif(command.startswith("dir")):
            temp = dirOrfile(command.split(' ')[-1])

            if(temp.name not in currentDir.subDirs):
                currentDir.subDirs.append(temp.name)
                print("New subdir", temp.name)
                nDirs+=1
            else:
                print(temp.name, "found")

        else:
            name = command.split(' ')[-1]
            size = command.split(' ')[0]
            temp = dirOrfile(temp)

            if(name not in currentDir.files):
                temp.size = int(size)
                temp.name = name
                currentDir.size += temp.size
                currentDir.files.append(temp.name)
                print("New file", temp.name, "with size", temp.size)
                print(currentDir.name, "size grows to", currentDir.size)
            else:
                print(name, "found")
                
    #TODO: dir.size = subDirs.size
        
    

            


            

class dirOrfile():
    name = None
    parentDir = None
    subDirs = []
    files = []
    size = 0
    visited = 0

    def __init__(self, name, parentDir=None, subDirs=[None], files=[None], size=0):
        self.name = name
        self.parentDir = parentDir
        self.subDirs = subDirs
        self.files = files
        self.size = size
'''
    def cons(self, name, parentDir, subDirs, files, size):
        self.name = name
        self.parentDir = parentDir
        self.subDirs = subDirs
        self.files = files
        self.size = size    
        return self
'''
if __name__ == "__main__":
    main()
