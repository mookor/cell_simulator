import numpy as np 
import cv2
import world
import cell
import random

width = 480
height = 640
cells =[]
for i in range(1135):
    photo = random.randint(0,1)
    hunt = random.randint(0,1)
    start_x = random.randint(0,width)
    start_y = random.randint(0,height)
    size = random.randint(3,6)
    cells.append(cell.Cell(photo,hunt,size,50,[start_x,start_y]))
simulation = world.World(width,height,cells)



while True:
    window = simulation.window
    cv2.imshow("simulation", window)
    simulation.random_move()
    key = cv2.waitKey(1)
    if key == ord("q"):
        break