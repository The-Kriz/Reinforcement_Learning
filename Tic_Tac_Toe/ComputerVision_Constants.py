import numpy as np
from pyniryo import *
from pyniryo.vision import *



# Blue color range
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])
Blue_Colour = [lower_blue,upper_blue]


# Red color range
lower_red = np.array([0, 50, 50])
upper_red = np.array([180, 255, 255])
Red_Colour = [lower_red,upper_red]

# Green color range
lower_green = np.array([0, 100, 100])
upper_green = np.array([70, 255, 255])
Green_Colour = [lower_green,upper_green]


Square_Block_ContourArea_Range = [1450,1700]
Circle_Block_ContourArea_Range = [800,1150]

#Objects
Circle_Block = ObjectShape.CIRCLE
Square_Block = ObjectShape.SQUARE
Red_Block = ObjectColor.RED
Blue_Block = ObjectColor.BLUE
Green_Block = ObjectColor.GREEN

Robot_Block_Shape = ObjectShape.SQUARE
Robot_Block_Shape_Str = "SQUARE"
Robot_Block_Colour = ObjectColor.BLUE
Robot_Block_Colour_Str = "BLUE"

Human_Block_Shape = ObjectShape.CIRCLE
Human_Block_Shape_Str = "CIRCLE"
Human_Block_Colour = ObjectColor.RED
Human_Block_Colour_Str = "RED"

