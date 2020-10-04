# Set up Lidar stuff
import math

def test():
    L = LIDAR()
    L.run()

class LIDAR():
    def __init__(self):
        self.phi = 0.0
        self.theta = 0.0
        self.maxRange = 12.0
        self.phiBounds = [0, 360]
        self.thetaBounds = [0, 180]
        self.step = 45
        #plus some other factors

    def rotate(self, phi, theta):
        self.phi = phi
        self.theta = theta

    def collectData(self):
        return self.phi, self.theta, self.maxRange

    def run(self):
        for i in range(*self.phiBounds, self.step):
            for j in range(*self.thetaBounds,self.step):
                self.rotate(i,j)
                print(self.collectData())

if __name__ == "__main__":
    test()