
class LIDAR():
    def __init__(self, x = 0.0, y = 0.0, z= 0.0, min = 1.0, max = 12.0):
        self.x = x
        self.y = y
        self.z = z
        self.min = min
        self.max = max
        self.ping = lambda theta, phi : theta * phi

    def cast_ray(self, phi = 0.0, theta = 0.0):
        return self.ping(phi, theta)

def test():
    lidar = LIDAR()
    for i in range(9):
        print( lidar.cast_ray(1.0, i) )

if __name__ == "__main__":
    test()