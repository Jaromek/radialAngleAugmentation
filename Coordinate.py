import math

class Coordinate:

    r = 1
    phi = 0

    def __init__(self, x, y):
        self.setXY(x, y)

        
    def getXY(self):
        x = self.r * math.cos(self.phi)
        y = self.r * math.sin(self.phi)
        return [x, y]

    def setXY(self, x, y):

        self.r = math.sqrt(x**2 + y**2)
        self.phi = math.acos(x/self.r)
        if y < 0:
            self.phi = 2*math.pi - self.phi

    def getR(self):
        return self.r
    
    def getPhi(self):
        return self.phi

    def setR(self, r):
        self.r = r

    def setPhi(self, phi):
        self.phi = phi

    def section_angle(n_angles):
        return 2*math.pi / n_angles

    def which_section(self, n_angles):
        return next(angle for angle in range(n_angles) if self.phi < angle * Coordinate.section_angle(n_angles))
