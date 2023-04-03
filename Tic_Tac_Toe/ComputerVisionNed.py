import cv2
import numpy as np
from pyniryo import *
from pyniryo.vision import *
from ComputerVision_Constants import *
from Ned_Constants import *

def initializeCamera(Client):
    """
    Staring Camera calibration
    :param Client:
    :return: mtx, dist
    """
    mtx, dist = Client.get_camera_intrinsics()
    return mtx, dist

def imageCapture(Client,ImageType="undistort",Display=False):
    """
    Capture image using Robot camera
    and Display image if needed

    :param Client:
    :param ImageType: compressed,uncompress,undistort,both
    :param Display: Boolean
    :return: Image
    """
    img_compressed = Client.get_img_compressed()
    if ImageType == "compressed":
        Image = img_compressed
    elif ImageType == "uncompress":
        Image = uncompress_image(img_compressed)
    elif ImageType == "undistort":
        mtx, dist = initializeCamera(Client)
        Image = undistort_image((uncompress_image(img_compressed)), mtx, dist)
    elif ImageType == "both":
        mtx, dist = initializeCamera(Client)
        Image = concat_imgs(((undistort_image(img_compressed, mtx, dist)), img_undistort))

    if Display == True:
        displayImage(Image)

    return Image

def displayImage(Image,Wait=False):
    """
    Displays Image
    :param Image:
    :return:
    """
    if Wait == True:
        show_img_and_wait_close("Robot_Cam", Image)
    elif Wait == False:
        show_img("Robot_Cam", Image)

def workSpaceImageTrim(Client,Image=None):
    """
    Trim image into workspace (200,200)
    :param Client:
    :param Image:
    :return: Workspace
    """
    if Image is None:
        Image = imageCapture(Client)
    workspace_found, res_img_markers = debug_markers(Image)
    # Trying to extract workspace if possible
    if workspace_found:
        workspace_Image = extract_img_workspace(Image, workspace_ratio=1.0)
        return workspace_Image
    else :
        return None

def findMarkers(Client, Image=None):
    """

    :param Client:
    :param Image:
    :return: workspace_found: Bool, res_img_markers: Image
    """
    if Image is None :
        Image = imageCapture(Client)
    workspace_found, res_img_markers = debug_markers(Image,workspace_ratio=1.0)
    return workspace_found, res_img_markers

def positionCordinates(Image,MaskColour,shape, MarkerReturn = False, MaskReturn = False):
    """
    Finds shape and colour and return array of positions (x,y) and images
    :param Image:
    :param MaskColour:
    :param shape:
    :param MarkerReturn:
    :return: center_x, center_y, markerd_img
    """
    hsv_img = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
    masked_img = cv2.inRange(hsv_img, MaskColour[0], MaskColour[1])
    contours, _ = cv2.findContours(masked_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = []
    filtered_contours_locations = []
    if shape == "SQUARE":
        MinContourArea = Square_Block_ContourArea_Range[0]
        MaxContourArea = Square_Block_ContourArea_Range[1]
    elif shape == "CIRCLE":
        MinContourArea = Circle_Block_ContourArea_Range[0]
        MaxContourArea = Circle_Block_ContourArea_Range[1]
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > MinContourArea and area < MaxContourArea:
            filtered_contours.append(contour)

    markerd_img = Image.copy()

    for contour in filtered_contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
            cv2.circle(markerd_img, (center_x, center_y), 5, (0, 255, 0), -1)
            filtered_contours_locations.append((center_x,center_y))


    if MaskReturn == True and MarkerReturn == True:
        return filtered_contours_locations, markerd_img , masked_img

    if MarkerReturn == True:
        return filtered_contours_locations, markerd_img

    if MaskReturn == True:
        return filtered_contours_locations, masked_img

    else:
        return filtered_contours_locations

def boardCellDivision(Image):
    """
    finds the x0 y0 x2 y2 of each cell and returns in an array
    :param Image:
    :return: array of all coordinates (x0,y0,x2,y2) of each cell in a single array
    """
    height, width, _ = Image.shape
    cell_width = width // 3
    cell_height = height // 3
    cell_coords = []
    for i in range(3):
        for j in range(3):
            x1 = j * cell_width
            y1 = i * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            cell_coords.append((x1, y1, x2, y2))
    return cell_coords

def FindCell(Image,positionCordinates):
    """
    checks the position of block in the cell and return cell address
    :param Image:
    :param positionCordinates: array [x,y] of the block
    :return: cell address
    """
    height, width, _ = Image.shape
    cell_size = (width // 3, height // 3)
    X_Cordinate,Y_Cordinate = positionCordinates[0],positionCordinates[1]
    Column_Id = X_Cordinate // cell_size[0]
    Row_Id = Y_Cordinate // cell_size[1]

    return Row_Id, Column_Id

def getMatrix(Image = None,Client = None, ImgReturn = False):
    """
    from the image, finds the cell location of each block and return matrix with 1(Robot) 0(No bloock) -1(Human)
    :param Image:
    :param Client if no image given
    :param if image return is needed
    :return: Matrix of size 3x3 with location of each block
    """
    if Image is None:
        Image =  workSpaceImageTrim(Client)
    filtered_contours_locations_Circle_Red, markerd_img_Circle_Red , masked_img_Circle_Red = positionCordinates(Image,Red_Colour,shape= "CIRCLE", MaskReturn = True, MarkerReturn= True)
    filtered_contours_locations_Square_Blue, markerd_img_Square_Blue , masked_img_Square_Blue = positionCordinates(Image,Blue_Colour,shape= "SQUARE", MaskReturn = True, MarkerReturn= True)
    matrix = [["0","0","0"],
              ["0","0","0"],
              ["0","0","0"]]
    for i in filtered_contours_locations_Square_Blue:
        row_idx, col_idx = FindCell(Image, i)
        matrix[row_idx][col_idx] = "1"
    for i in filtered_contours_locations_Circle_Red:
        row_idx, col_idx = FindCell(Image, i)
        matrix[row_idx][col_idx] = "-1"
    if ImgReturn == True :
        return matrix , markerd_img_Circle_Red,masked_img_Circle_Red,markerd_img_Square_Blue,masked_img_Square_Blue
    else:
        return matrix

def robotGameCellReset(Client):
    """
    finds all the Blocks
    picks all Robot_Block one by one
        place it in *Place_To_Tray*
    picks all Human_Block one by one
        place it in *Place_To_Tray*

    :param Client:
    :return:
    """
    Client.move_pose(Board_Observation_Pose)
    Client.wait(Robot_Sleep)

    while True:
        Robot_object_found, _,_ = Client.vision_pick(Robot_Workspace,
                                                     height_offset=0.0,
                                                     shape=Robot_Block_Shape,
                                                     color=Robot_Block_Colour)
        print(Robot_object_found)
        if Robot_object_found:
            Client.place_from_pose(Place_To_Tray)
            Client.wait(Robot_Sleep)
        else:
            break

        Client.move_pose(Board_Observation_Pose)
        Client.wait(Robot_Sleep)

    while True:
        Human_object_found,_,_ =  Client.vision_pick(Robot_Workspace,
                                                    height_offset=0.0,
                                                     shape=Human_Block_Shape)
                                                    #,color=Human_Block_Colour)

        if Human_object_found:
            Client.place_from_pose(Place_To_Human_Tray)
            Client.wait(Robot_Sleep)
        else:
            break

        Client.move_pose(Board_Observation_Pose)
        Client.wait(Robot_Sleep)

def pickOnVision(Client,Robot_Workspace,height_offset=0.0,Block_shape = ObjectShape.ANY, Block_color = ObjectColor.ANY):  # neeeed to fix
    """
    Check if the specified block is preset if present pick and return True if present else fales
    :param Client:
    :param Robot_Workspace: work space to pick from
    :param height_offset:
    :param Block_shape: shape of the block to pick
    :param Block_color: colour of the block to pick
    :return:
    """
    Robot_object_found, _, _ = Client.vision_pick(Robot_Workspace,
                                                 height_offset=0.0,
                                                 shape=Block_shape,
                                                 color=Block_color)
    if Robot_object_found:
        return True
        # Client.place_from_pose(Place_To_Tray)
        # Client.wait(Robot_Sleep)
    else:
        return  False

    # Client.move_pose(Board_Observation_Pose)
    # Client.wait(Robot_Sleep)
