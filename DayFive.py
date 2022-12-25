def createStacks(crates):
    stacks = []
    for i in range(int(len(crates[-1]) / 4) + 1):
        stacks.append([])
    for i in range(len(crates)):
        for j in range(len(crates[i])):
            if crates[i][j].isalpha():
                stacks[int(j / 4)].append(crates[i][j])
    for i in stacks:
        i.reverse()
    return stacks

def partOne(movement, lines):
    topCrates = ""
    stacks = createStacks(list(lines[0].split("\n")))
    for i in range(len(movement)):
        moves = movement[i].split()
        number = int(moves[1])
        fromStack = int(moves[3])
        toStack = int(moves[5])
        for j in reversed(range(number)):
            popped = stacks[fromStack - 1].pop()
            stacks[toStack - 1].append(popped)

    for i in stacks:
        topCrates += i[-1]
    return topCrates

def partTwo (movement, lines):
    topCrates = ""
    stacks = createStacks(list(lines[0].split("\n")))
    r = []
    for i in range(len(movement)):
        moves = movement[i].split()
        number = int(moves[1])
        fromStack = int(moves[3])
        toStack = int(moves[5])
        for j in reversed(range(number)):
            popped = stacks[fromStack - 1].pop()
            r.append(popped)
        r.reverse()
        for j in range(number):
            stacks[toStack - 1].append(r[j])

    for i in stacks:
        topCrates += i[-1]
    return topCrates

def main():
    with open('Input.txt') as f:
        lines = f.read().split("\n\n")
        crates = list(lines[0].split("\n"))
        crates.pop()
        movement = list(lines[1].split("\n"))

        print("Cargo Crane Arrangement: " + partOne(movement, lines))
        print("CrateMover 9001 Arrangement: " + partTwo(movement, lines))
        # print(createStacks(crates))






if __name__ == "__main__":
    main()
