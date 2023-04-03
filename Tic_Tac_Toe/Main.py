from Ned_Niryo import *
from ComputerVisionNed import *
import time
from MinMax import *
from Tic_Tac_Toe import *

Ned = robotStart()
robotBackHome(Ned)
robotObservationPose(Ned)
time.sleep(1)
count = 0
Game_End_State = False
while True:
    matrix = getMatrix(Client=Ned)
    Game_End_State = isWinner(matrix,count)
    if count < 8 and Game_End_State == False:
        player = WhoHasToPlay(count)
        if player == "Human":
            played = input("Press enter after your move")
#             time.sleep(2)
#             while True:
#                 matrix1 = getMatrix(Client=Ned)
#                 if matrix1 != matrix :
#                     break
#                 else:
#                     time.sleep(1)
        else :
            bestMove = findBestMove(matrix)
            robotPlaceOnCell(Ned,bestMove)
        count += 1
    else:
        break
report(count, Game_End_State)
time.sleep(1)
robotStop(Ned)



