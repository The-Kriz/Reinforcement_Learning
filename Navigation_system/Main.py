import cv2
from Path import *
from Computer_Vision import *
from Tetrix_Motion import *

## no HC05 part

image = cv2.imread('Testing_Images/aruco6.jpg')
cv2.imshow("Original image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped_image = ArucoCropImage(image)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

ids = DetectAruco(cropped_image)
val = SplitImage(cropped_image)
grid = ArucoIdToGrid(val)
print(grid)

env, qtable = gymActivation(grid)
sequence = seq(env, qtable)
path = PathText(sequence)

movement = motionPlan(path)
print(movement)

btModule = btConnect()
sendMovement(movement, btModule)
btDisconnect(btModule)
