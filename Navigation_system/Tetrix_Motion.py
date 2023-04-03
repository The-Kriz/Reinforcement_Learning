import serial
from time import sleep

'''
Forward   = 1
Left      = 2
Right     = 3
Backward  = 4
'''

#
# def motionPlan(path):
#     i = 0
#     bot_movements = []
#     if path[i] == "Left":
#         bot_movements.append("2")
#     elif path[i] == "Right":
#         bot_movements.append("3")
#     elif path[i] == "Backward":
#         bot_movements.append("4")
#
#     while True:
#         if bot_movements[i] != "4":
#             bot_movements.append("1")
#             i += 1
#         if i >= len(path):
#             if path[i-1] == "Left":
#                 bot_movements.append("3")
#             elif path[i-1] == "Right":
#                 bot_movements.append("2")
#             break
#         if path[i-1] != path[i] or i < len(path):
#             if path[i-1] == "Left" and path[i] == "Forward":
#                 bot_movements.append("3")
#             elif path[i-1] == "Left" and path[i] == "Right":
#                 bot_movements.append("3")
#                 bot_movements.append("3")
#             elif path[i-1] == "Right" and path[i] == "Forward":
#                 bot_movements.append("2")
#             elif path[i-1] == "Right" and path[i] == "Left":
#                 bot_movements.append("2")
#                 bot_movements.append("2")
#             elif path[i-1] == "Forward" and path[i] == "Right":
#                 bot_movements.append("3")
#             elif path[i-1] == "Forward" and path[i] == "Left":
#                 bot_movements.append("2")
#     return bot_movements

#
#
# def motionPlan(path):
#     i = 0
#     bot_movements = []
#     if path[i] == "Left":
#         bot_movements.append("2")
#     elif path[i] == "Right":
#         bot_movements.append("3")
#     elif path[i] == "Backward":
#         bot_movements.append("4")
#     elif path[i] == "Forward":
#         bot_movements.append("1")
#     i += 1
#     while True:
#         if i >= len(path):
#             break
#         if path[i - 1] != path[i] or i < len(path):
#             if path[i - 1] == "Left" and path[i] == "Forward":
#                 bot_movements.append("3")
#                 bot_movements.append("1")
#             elif path[i - 1] == "Left" and path[i] == "Right":
#                 bot_movements.append("3")
#                 bot_movements.append("3")
#                 bot_movements.append("1")
#             elif path[i - 1] == "Right" and path[i] == "Forward":
#                 bot_movements.append("2")
#                 bot_movements.append("1")
#             elif path[i - 1] == "Right" and path[i] == "Left":
#                 bot_movements.append("2")
#                 bot_movements.append("2")
#                 bot_movements.append("1")
#             elif path[i - 1] == "Forward" and path[i] == "Right":
#                 bot_movements.append("3")
#                 bot_movements.append("1")
#             elif path[i - 1] == "Forward" and path[i] == "Left":
#                 bot_movements.append("2")
#                 bot_movements.append("1")
#             elif path[i - 1] == "Backward" and path[i] == "Left":
#                 bot_movements.append("2")
#                 bot_movements.append("1")
#             elif path[i - 1] == "Backward" and path[i] == "Right":
#                 bot_movements.append("3")
#                 bot_movements.append("1")
#             elif path[i - 1] == path[i]:
#                 if path[i] == "Backward":
#                     bot_movements.append("4")
#                 else:
#                     bot_movements.append("1")
#             i += 1
#     return bot_movements
#


def motionPlan(path):
    i = 0
    botFace = "NORTH"
    bot_movements = []
    if path[i] == "Left":
        botFace = "WEST"
        bot_movements.append("2")
        bot_movements.append("1")
    elif path[i] == "Right":
        botFace = "EAST"
        bot_movements.append("3")
        bot_movements.append("1")
    elif path[i] == "Backward":
        bot_movements.append("4")
    elif path[i] == "Forward":
        bot_movements.append("1")
    i += 1
    while True:
        if i >= len(path):
            break
        if path[i - 1] != path[i] or i < len(path):
            if path[i - 1] == "Left" and path[i] == "Forward":
                botFace = "NORTH"
                bot_movements.append("3")
                bot_movements.append("1")
            elif path[i - 1] == "Left" and path[i] == "Right":
                botFace = "EAST"
                bot_movements.append("3")
                bot_movements.append("3")
                bot_movements.append("1")
            elif path[i - 1] == "Left" and path[i] == "Backward":
                # if botFace == "WEST:
                #     bot_movements.append("2")
                #     bot_movements.append("1")
                botFace = "SOUTH"
                bot_movements.append("2")
                bot_movements.append("1")
            elif path[i - 1] == "Right" and path[i] == "Forward":
                botFace = "NORTH"
                bot_movements.append("2")
                bot_movements.append("1")
            elif path[i - 1] == "Right" and path[i] == "Left":
                botFace = "WEST"
                bot_movements.append("2")
                bot_movements.append("2")
                bot_movements.append("1")
            elif path[i - 1] == "Right" and path[i] == "Backward":
                botFace = "SOUTH"
                bot_movements.append("3")
                bot_movements.append("1")
            elif path[i - 1] == "Forward" and path[i] == "Right":
                botFace = "EAST"
                bot_movements.append("3")
                bot_movements.append("1")
            elif path[i - 1] == "Forward" and path[i] == "Left":
                botFace = "WEST"
                bot_movements.append("2")
                bot_movements.append("1")
            elif path[i - 1] == "Backward" and path[i] == "Left":
                if botFace == "SOUTH":
                    bot_movements.append("3")
                    bot_movements.append("1")
                else:
                    bot_movements.append("2")
                    bot_movements.append("1")
                botFace = "WEST"

            elif path[i - 1] == "Backward" and path[i] == "Right":
                if botFace == "SOUTH":
                    bot_movements.append("2")
                    bot_movements.append("1")
                    botFace = "EAST"

                else:
                    bot_movements.append("3")
                    bot_movements.append("1")
                    botFace = "EAST"

            elif path[i - 1] == path[i]:
                if path[i] == "Backward":
                    bot_movements.append("4")
                else:
                    bot_movements.append("1")
        i += 1
    reversedMovement = bot_movements[::-1]
    return reversedMovement


def sendMovement(bot_path, btModule):
    bot_movements_str = ''.join(bot_path)
    encodedVal = bot_movements_str.encode()
    btModule.write(encodedVal)


def turnOfTetrix(btModule):
    stop = "9"
    btModule.write(stop.encode())


def btConnect():
    # btModule = serial.Serial('/dev/tty.HC-05-DevB', 9600) # Linux
    btModule = serial.Serial('COM17', 9600)   # Windows
    if btModule.is_open:
        print('Connected to BT module')
    else:
        print('Failed to connect to BT module')
    sleep(3)
    return btModule


def btDisconnect(btModule):
    btModule.close()
