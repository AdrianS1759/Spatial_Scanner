import math

class Point():
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

class Line():
    def __init__(self, origin, end):
        #Make a line to paremetirize so I can have a local grid set

        self.origin = origin
        self.end = end

        self.delta = {"x": end.x - origin.x, 
                      "y": end.y - origin.y, 
                      "z": end.z - origin.z}

        self.line = lambda t : [self.origin.x + t * delta["x"], 
                                self.origin.y + t * delta["y"],
                                self.origin.z + t * delta["z"]]

    def getXYZ(self, t = 0.5):
        pass
        


class Corner():
    def __init__(self, origin, p1, p2, p3):
        self.origin = origin
        self.v1 = Line(origin, p1)
        self.v2 = Line(origin, p2)
        self.v3 = Line(origin, p3)

class Wall():
    def __init__(self, origin, p1, p2):
        self.origin = origin
        self.corner1 = p1
        self.corner2 = p2
        self.normal = self.find_normal(origin, corner1, corner2)

    def find_normal(self, origin, corner1, corner2):
        v1 = [corner1.x - origin.x, corner1.y - origin.y, corner1.z - origin.z]
        v2 = [corner2.x - origin.x, corner2.y - origin.y, corner2.z - origin.z]

        a = v1[1] * v2[2] - v1[2] * v2[1]
        b = v1[0] * v2[2] - v1[2] * v2[0]
        c = v1[0] * v2[1] - v1[1] * v2[0]

        return [a, b, c]

class Room():
    def __init__(self, ):
        pass


def test():
    c1 = Point()
    c2 = Point(1.0, 0.0, 0.0)
    c3 = Point(0.0, 1.0, 0.0)

    print( w.normal )


if __name__ == "__main__":
    test()