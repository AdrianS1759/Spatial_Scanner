
class simulator():
    def set_plane(self, coefficents):
        a = coefficents[0]
        b = coefficents[1]
        c = coefficents[2]
        self.equation = lambda x, y, z: (a * x) + (b * y) + (c * z) + self.error()
    def error(self):
        return 0.0
    def get_Distance(self, theta, phi):
        pass