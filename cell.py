import numpy as np

class Cell:
    def __init__(self, photo, hunt, size, energy,start_position):
        start_position = np.array(start_position)
        self.photo = photo
        self.hunt = hunt
        self.size = size
        self.energy = energy
        self.position = np.array([start_position,start_position + size])
        if self.energy > 100:
            self.energy = 100
        red,green,blue = 0,0,0
        if self.hunt:
            red = 255
        if self.photo:
            green = 255
        if not self.hunt and not self.photo:
            blue = 255
        self.color = (blue,green,red)
            
    def move(self,vec_x,vec_y,width,height):
        start_pos_x1 = self.position[0][0]
        start_pos_y1 = self.position[0][1]
        
        start_pos_x2 = self.position[1][0]
        start_pos_y2 = self.position[1][1]
        
        
        new_x1 = start_pos_x1 + vec_x
        new_x2 = start_pos_x2 + vec_x
        new_y1 = start_pos_y1 + vec_y
        new_y2 = start_pos_y2 + vec_y
        if new_x2 >= height or new_x1 <= 0 or new_y1 <= 0 or new_y2 >=width:
            new_x1 = self.position[0][0]
            new_y1 = self.position[0][1]
            new_x2 = self.position[1][0]
            new_y2 = self.position[1][1]
        else:
            new_x1 = start_pos_x1 + vec_x
            new_x2 = start_pos_x2 + vec_x
            new_y1 = start_pos_y1 + vec_y
            new_y2 = start_pos_y2 + vec_y         
        self.position = np.array([[new_x1,new_y1],[new_x2,new_y2]])