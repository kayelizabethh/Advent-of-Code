import string

def matches(c1, c2):
    match = ''
    for i in range(len(c1)):
        for j in range(len(c2)):
            if c1[i] == c2[j]:
                match = c1[i]
    return match

def alphabet():
    letters = list(string.ascii_letters)
    priorities = {}
    for i in range(len(letters)):
        priorities[letters[i]] = i+1
    return priorities

def charArr(lines):
    group = []
    outer = []
    for i in range(int(len(lines) / 3)):
        group.append(lines[i*3:i*3+3])
    for i in range(len(group)):
        inner = []
        for j in range(3):
            inner.append(list(group[i][j]))
        outer.append(inner)
    return outer

def threeElves(lines):
    group = charArr(lines)
    totalScore = 0
    for i in range(len(group)):
        g1 = group[i][0]
        for j in range(len(g1)):
            if g1[j] in group[i][1] and g1[j] in group[i][2]:
                match = g1[j]
        totalScore += (alphabet().get(match))
    return totalScore

def main():
    with open('Input.txt') as f:
        lines = f.read().split()
        # print(str(threeElves(lines)))


        priorities = []
        length = len(lines)
        for i in range(length):
            rucksack = lines[i]
            half = int(len(rucksack) / 2)
            c1 = list(rucksack[slice(0, half)])
            c2 = list(rucksack[slice(half, half * 2)])
            priorities.append(alphabet().get(matches(c1, c2)))

        print("The sum of the compartments is: " + str(int(sum(priorities))))
        print("The sum of the three elves is: " + str(threeElves(lines)))

if __name__ == "__main__":
    main()