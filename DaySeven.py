root = []
currentLine = 0


def fileSum(lines):
    global currentLine
    total = 0
    i = 0
    while i < len(lines):
        commands = lines[i].split(" ")
        if commands[0].isdigit():
            total += int(commands[0])
        elif len(commands) == 3 and commands[2] == '..':
            i += 1
            break
        elif commands[1] == 'cd':
            subdir = fileSum(lines[i + 1:])
            total += subdir
            i += currentLine
            root.append(subdir)
        i += 1
    currentLine = i
    return total


with open('Input.txt') as f:
    lines = f.read().split("\n")
    files = 0
    partOne = 0
    fileSum(lines)
    for i in root:
        if i < 100000:
            partOne += i

    # this returns the total value of the sum off the files within the root list
    # within the root list I am creating other lists that represent each folder
    # when printing out the root in the open() method, it should list all the folders and their sizes
    print("the total size of directories under 100,000 is " + str(partOne))

    root.sort()
    for f in root:
        if f > 30000000 - (70000000 - fileSum(lines)):
            print("the total size of directory to delete is is " + str(f))
            break
