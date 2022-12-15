calories = 0

with open('Input.txt') as f:
    lines = f.read().split("\n")
    elves = []
    threeElves = []
    for i in range(len(lines)):
        if(lines[i].isdigit()):
            elves.append(int(lines[i]))
        else:
            calories = sum(elves)
            threeElves.append(calories)
            elves.clear()
    calories = sum(elves)
    threeElves.append(calories)
    sortedList = sorted(threeElves)
    total = sum(sortedList[-3:])
    print('elf with the most calories: ' + str(sortedList[-1]))
    print('total of the top three elves: ' + str(total))











