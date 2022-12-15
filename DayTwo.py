with open('Input.txt') as f:
    lines = f.read().split("\n")

def rockpaperscissors():
    partOne = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }

    partTwo = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
        'draw': 3,
        'win': 6,
        'lose': 0
    }

    totalScore = 0
    newScore = 0

    for i in range(len(lines)):
        rounds = lines[i].split(" ")
        opponent = partOne.get(rounds[0])
        player = partOne.get(rounds[1])
        totalScore += partOne.get(player)
        totalScore += (gameLogic(opponent, player))

        move = partTwo.get(rounds[1])
        points = secondGameLogic(opponent, move)
        newScore += partTwo.get(move) + partOne.get(points)

    print("Round One: " + str(totalScore))
    print("Round Two: " + str(newScore))

def gameLogic(opponent, player):
    score = 0
    if opponent == player:
        score += 3
    if opponent == 'rock' and player == 'paper':
        score += 6
    if opponent == 'paper' and player == 'scissors':
        score += 6
    if opponent == 'scissors' and player == 'rock':
        score += 6
    return score

def secondGameLogic(opponent, move):
    turn = ''
    if move == 'draw':
        turn = opponent
    elif move == 'win':
        if opponent == 'rock':
            turn = 'paper'
        elif opponent == 'paper':
            turn = 'scissors'
        elif opponent == 'scissors':
            turn = 'rock'
    elif move == 'lose':
        if opponent == 'rock':
            turn = 'scissors'
        elif opponent == 'paper':
            turn = 'rock'
        elif opponent == 'scissors':
            turn = 'paper'
    return turn

def main():
    rockpaperscissors()

if __name__ == "__main__":
    main()




