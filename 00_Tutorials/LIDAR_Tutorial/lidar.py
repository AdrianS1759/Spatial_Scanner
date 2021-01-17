# Set up Lidar stuff
import math
import numpy as np
import Room

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
        self.n = 10
        self.room = Room()
        #plus some other factors

    def fetch(self, phi, theta):
        distance = self.room.RoomData(phi, theta)

        if distance > self.maxRange:
            return self.maxRange

        return distance

    def rotate(self, phi, theta):
        self.phi = phi
        self.theta = theta

    def collectData(self):
        distance = self.fetch(self.phi, self.theta)
        return self.phi, self.theta, distance

    def run(self):
        for i in np.linspace(*self.phiBounds, num = self.n, endpoint=False):
            for j in np.linspace(*self.thetaBounds, num = self.n, endpoint=False):
                self.rotate(i,j)
                print(self.collectData())

if __name__ == "__main__":
    test()