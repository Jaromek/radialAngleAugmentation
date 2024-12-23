import math

class Augmentacja:
    def __init__(self, x, y):

        self.r = math.sqrt(x**2 + y**2)
        self.phi = math.acos(x/self.r)
        if y < 0:
            self.phi = 2*math.pi - self.phi
        
    def getXY(self, r, phi):
        x = r * math.cos(phi)
        y = r * math.sin(phi)
        return x, y