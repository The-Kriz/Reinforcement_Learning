from pyniryo import *


Robot_Ip_Address = "169.254.200.200" # Robot's ip address

Robot_Workspace = "Tic_Tac_Toe" # Robot's Workspace

Robot_Sleep = 0.5 #seconds
Gripper_Tool_Speed = 500 #Tool gripper speed
Max_Board_Pick_Count = 9


Home = PoseObject(
                    x=0.30, y=0.0, z=0.15,
                    roll=0, pitch=1.57, yaw=0.0,
                    )


Pick_From_Tray = PoseObject(
                            x=0.218, y=0.258, z=0.134,
                            roll = 2.162, pitch = 1.078, yaw = 2.132
                           )


Place_To_Tray = PoseObject(
                            x=0.061, y=0.257, z=0.192,
                            roll=-2.588, pitch=0.92, yaw=2.023,
                            )

Place_To_Human_Tray = PoseObject(
                                x=0.266, y=-0.17, z=0.12,
                                roll=2.88, pitch=1.56, yaw=2.892,
                              )


Board_Observation_Pose = PoseObject(
                                    x=-0.0178, y=-0.1092, z=0.4264,
                                    roll = -0.114, pitch = 1.444, yaw = -1.732
                                    )

# Place Pose for each cell on the board
Board_place_pose_cell_00 = PoseObject(
                                        x=0.0346, y=-0.3194, z=0.0965,
                                        roll = -0.305, pitch = 1.561, yaw = -1.856
                                    )

Board_place_pose_cell_01 = PoseObject(
                                        x = -0.0186, y = -0.3207, z = 0.0966,
                                        roll = -0.190, pitch = 1.500, yaw = -1.686
                                    )

Board_place_pose_cell_02 = PoseObject(
                                        x = -0.0686, y = -0.3132, z = 0.0972,
                                        roll = -0.316, pitch = 1.486, yaw = -1.840
                                    )

Board_place_pose_cell_10 = PoseObject(
                                        x = 0.0363, y = -0.2656, z = 0.0964,
                                        roll = -3.015, pitch = 1.562, yaw = 1.703
                                    )

Board_place_pose_cell_11 = PoseObject(
                                        x = -0.0167, y = -0.2657, z = 0.0965,
                                        roll = 3.135, pitch = 1.560, yaw = 1.561
                                    )

Board_place_pose_cell_12 = PoseObject(
                                        x = -0.0631, y = -0.2595, z = 0.0963,
                                        roll = -0.257, pitch = 1.544, yaw = -1.828
                                    )

Board_place_pose_cell_20 = PoseObject(
                                        x = 0.0425, y = -0.2022, z = 0.0956,
                                        roll = 0.171, pitch = 1.543, yaw = -1.373
                                    )

Board_place_pose_cell_21 = PoseObject(
                                        x = -0.0101, y = -0.1969, z = 0.0957,
                                        roll = -0.079, pitch = 1.558, yaw = -1.642

                                    )

Board_place_pose_cell_22 = PoseObject(
                                        x = -0.0573, y = -0.1899, z = 0.0959,
                                        roll = -0.326, pitch = 1.535, yaw = -1.870
                                    )

