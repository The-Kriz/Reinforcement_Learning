# Tic Tac Toe Game Logic

def main(matrix):
    full = isFull(matrix,count)

def WhoHasToPlay(count):
    """
    Gets the count and tells who has to play next
    :param count:
    :return: "Human" or "Ned"
    """
    if count % 2 == 0:
        player = "Human"
    elif count % 2 == 1:
        player = "Ned"
    print("It is" + player + " turn.")
    return player

def isFull(matrix,count):
    winner = False
    if count == 8:
        print("The matrix is full. Game over.")
        if winner == False:
            print("There is a tie. ")
    else:
        WhoHasToPlay(count)

        winner = isWinner(matrix,count)
        count += 1
        if winner == True:
            print("Game over.")
            report(count, winner)

def isWinner(matrix,count):
    """
    checks all the possible win sequence and return if anyone won
    :param matrix:
    :param count:
    :return: Bool True = player won
    """
    winner = False
    for row in range(0, 3):
        if (matrix[row][0] == matrix[row][1] == matrix[row][2] == "Ned"):
            winner = True

        elif (matrix[row][0] == matrix[row][1] == matrix[row][2] == "Human"):
            winner = True

    for col in range(0, 3):
        if (matrix[0][col] == matrix[1][col] == matrix[2][col] == "Ned"):
            winner = True
        elif (matrix[0][col] == matrix[1][col] == matrix[2][col] == "Human"):
            winner = True

    if matrix[0][0] == matrix[1][1] == matrix[2][2] == "Ned":
        winner = True

    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == "Human":
        winner = True

    elif matrix[0][2] == matrix[1][1] == matrix[2][0] == "Ned":
        winner = True

    elif matrix[0][2] == matrix[1][1] == matrix[2][0] == "Human":
        winner = True

    return winner

def report(count, winner):
    """
    Display who won or draw
    :param count:
    :param winner:
    :return:
    """
    if (winner == True) and (count % 2 == 1):
        print("Winner : Ned.")
    elif (winner == True) and (count % 2 == 0):
        print("Winner : Human.")
    else:
        print("Its a tie. ")

