import math

class Corner():
    def __init__(self, r = 0.0, phi = 0.0, theta = 0.0):
        self.r = r
        self.phi = phi
        self.theta = theta
    
    def toCartesean(self):
        return self.r * [
            math.sin(self.phi) * math.cos(self.theta) , 
            math.sin(self.phi) * math.sin(self.theta) , 
            math.cos(self.phi) ]
class Side():
    #Should I make it so it yields a line equation?
    def __init__(self, corner_1, corner_2):
        self.corner_1 = corner_1
        self.corner_2 = corner_2

class Wall():
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

class Room():
    def __init__(self, length, width, height, debugging):
        self.corners = [[length,0,0],
                        [0,width,0],
                        [0,0,height]] #This variable shall contain a vector that holds the length, width, and height of the room
        self.debugging = debugging
    
    def RoomData(self, phi, theta):
        #Set up my get function
        return 0.0

    def planeZ(self, gradient):
        return