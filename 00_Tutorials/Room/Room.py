class Room():
    def __init__(self, length, width, height, debugging):
        self.corners = [[length,0,0],
                        [0,width,0],
                        [0,0,height]] #This variable shall contain a vector that holds the length, width, and height of the room
        self.debugging = debugging
    
    def planeZ(self, gradient):
        return