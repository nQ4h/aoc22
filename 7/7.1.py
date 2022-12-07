def main():
    with open("t.txt", 'r') as fp:
        nLines = len(fp.readlines())
        currentDir = dirOrfile("root")
    for i in range(nLines):
        command = input()
        if(command == "$ cd .."):
            print("cd ..")
            currentDir = currentDir.parentDir
            print(currentDir.name)
        elif(command.startswith("$ cd")):
            temp = dirOrfile(command.split(' ')[-1])
            print("cd", temp.name)
            if (temp in currentDir.subDirs):
                currentDir = temp
                print(temp,"found")
            else:
                currentDir.subDirs.append(temp)
                temp.parentDir = currentDir
                currentDir = temp
                print("New subdir", temp.name)
        elif (command == "$ ls"):
            print("ls")
        elif(command.startswith("dir")):
            temp = dirOrfile(command.split(' ')[-1])
            if(temp not in currentDir.subDirs):
                currentDir.subDirs.append(temp.name)
                print("New subdir", temp.name)
        else:
            name = command.split(' ')[-1]
            size = command.split(' ')[0]
            temp = dirOrfile(temp)
            if(temp.name not in currentDir.files):
                temp.size = int(size)
                temp.name = name
                currentDir.size += temp.size
                print("New file", temp.name, "with size", temp.size)
                print(currentDir.name, "size grows to", currentDir.size)

            


            

class dirOrfile():
    name = None
    parentDir = None
    subDirs = []
    files = []
    size = 0

    def __init__(self, name, parentDir=None, subDirs=[], files=[None], size=0):
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
