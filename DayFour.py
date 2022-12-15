def main():
    with open('Input.txt') as f:
        lines = f.read().split()
        subset = 0
        overlap = 0
        for i in range(len(lines)):
            elf1 = lines[i].split(",")[0]
            elf2 = lines[i].split(",")[1]
            a1 = int(elf1.split("-")[0])
            a2 = int(elf1.split("-")[1])
            a3 = int(elf2.split("-")[0])
            a4 = int(elf2.split("-")[1])

            distances = [list(range(a1, a2 + 1)), list(range(a3, a4 + 1))]

            if all(x in distances[0] for x in distances[1]):
                subset += 1
            elif all(x in distances[1] for x in distances[0]):
                subset += 1

            if any(x in distances[0] for x in distances[1]):
                overlap += 1

    print("The number of completely overlapping pairs is " + str(subset))
    print("The sum of any pairs that overlap is " + str(overlap))


if __name__ == "__main__":
    main()
