import math

class Coordinate:

    r = 1
    phi = 0
    shiftPhi = 0
    

    def __init__(self, r, phi, polar = False):
        """
        konstruktor klasy. Zwraca współrzędne biegunowe jeśli polar = True, w przeciwnym wypadku zwraca współrzędne kartezjańskie
        """
        if polar:
            self.r = r
            self.phi = phi
        else:
            x = r
            y = phi
            self.setXY(x, y)
    

    def getXY(self):
        """
        zwraca współrzędne kartezjańskie punktu x i y w tablicy -> [x, y]
        """
        x = self.r * math.cos(self.phi - Coordinate.shiftPhi if self.phi - Coordinate.shiftPhi >= 0 else 2*math.pi + self.phi - Coordinate.shiftPhi)
        y = self.r * math.sin(self.phi - Coordinate.shiftPhi if self.phi - Coordinate.shiftPhi >= 0 else 2*math.pi + self.phi - Coordinate.shiftPhi)
        return [x, y]

    def setXY(self, x, y):
        """
        ustawia współrzędne biegunowe punktu na podstawie współrzędnych kartezjańskich x i y        
        """
        self.r = math.sqrt(x**2 + y**2)
        self.phi = math.acos(x/self.r) 
        if y < 0:
            self.phi = 2*math.pi - self.phi 

    def getR(self):
        return self.r
    
    def getPhi(self):
        return self.phi - Coordinate.shiftPhi if self.phi - Coordinate.shiftPhi >= 0 else 2*math.pi + self.phi - Coordinate.shiftPhi

    def setR(self, r):
        self.r = r

    def setPhi(self, phi):
        self.phi = phi 

    
