import numpy as np
import cv2
import random

class World:
    def __init__(self,width,height,Cells):
        self.width = width
        self.height = height
        self.Cells = Cells

        self.window = np.full((width,height,3),0,dtype=float)

    def random_move(self):
        for Cell in self.Cells:
            black_pose = Cell.position
            pt1 = (black_pose[0][0],black_pose[0][1])
            pt2 = (black_pose[1][0],black_pose[1][1])
            r = Cell.color[0]
            g = Cell.color[1]
            b = Cell.color[2]
            cv2.rectangle(self.window,pt1,pt2,(0,0,0),-1)
            vec_x = random.randint(-13,13)
            vec_y = random.randint(-7,7)
            Cell.move(vec_x,vec_y,self.width,self.height)
            pt1 = (Cell.position[0][0],Cell.position[0][1])
            pt2 = (Cell.position[1][0],Cell.position[1][1])
            
            cv2.rectangle(self.window, pt1, pt2,(r,g,b),-1)

