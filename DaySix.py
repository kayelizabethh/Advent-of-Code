def signal(lines, num):
    data = []
    marker = []
    counter = 3
    for i in range(len(lines)):
        data.append(lines[i])

    for i in range(num):
        marker.append(data[i])

    for i in range(len(data)):
        if not len(set(marker)) == len(marker):
            marker.pop(0)
            counter += 1
            marker.append(data[counter])
    return counter + 1

def main():
    with open('Input.txt') as f:
        lines = f.read()
        lines = list(lines)
        print('The number of characters needed is: ' + str(signal(lines, 4)))
        print('The number of characters needed is: ' + str(signal(lines, 14)))


if __name__ == "__main__":
    main()
