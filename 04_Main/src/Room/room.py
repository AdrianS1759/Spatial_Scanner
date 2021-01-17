class Point():
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def toList(self):
        return [self.x, self.y, self.z]

class Corner():
    def __init__(self, p0, neigbors):
        #will encrypt information on neighboring corners by storing the corresponding vector directions
        self.vectors = []
        self.p0 = p0
        self.lines = []
        for p in neigbors:
            self.vectors.append([p[0] - self.p0[0],
                                 p[1] - self.p0[1],
                                 p[2] - self.p0[2]] )

        for l in self.vectors:
            T = []
            for i in range( len(l) ):
                T.append( lambda t: self.p0[i] + t * l[i] )
            self.lines.append(T)


class Room():
    def __init__(self, x = 1.0, y = 1.0 , z = 1.0):
        


        self.walls = (  )
        