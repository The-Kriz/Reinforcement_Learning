from Computer_Vision_Constant import *
from Aruco_Perspective_Crop import *
from Tetrix_Motion import *
from Path import *
import cv2


image = cv2.imread('Testing_Images/aruco24.jpg')
cv2.imshow("Original image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
cropped_image = ArucoCropImage(image, CustomOrder=gridArucoID)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

ids = DetectAruco(cropped_image)
val, cellImage = SplitImage(cropped_image, imageReturn=True)
cv2.imshow("cell", cellImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

grid = ArucoIdToGrid(val)
print(grid)

env, qtable = gymActivation(grid)
sequence = seq(env, qtable)
path = PathText(sequence)

movement = motionPlan(path)
print(movement)

btModule = btConnect()
if btModule:
    sendMovement(movement, btModule)
    btDisconnect(btModule)
