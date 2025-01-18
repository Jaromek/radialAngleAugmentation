import math

class Coordinate:

    r = 1
    phi = 0
    shiftPhi = 0
    sectionID = 0
    subsectionID = 0
    global_subsectionID = 0
    colorSection = 0
    colorSubSection = 0

    

    def __init__(self, r: float, phi: float, polar = False, sectionID: int = 0, subsectionID: int = 0):
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
        
        self.sectionID = sectionID
        self.subsectionID = subsectionID
    

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

    def getSectionID(self):
        return self.sectionID
    
    def setSectionID(self, sectionID):
        self.sectionID = sectionID
    
    def setSubsectionID(self, subsectionID):
        self.subsectionID = subsectionID
            
    def getSubsectionID(self):
        return self.subsectionID
    
    def setSubsectionID(self, subsectionID):
        self.subsectionID = subsectionID

    def setGlobalSubsectionID(self, global_subsectionID):
        self.global_subsectionID = global_subsectionID

    def getGlobalSubsectionID(self):
        return self.global_subsectionID
    
    def getColorSection(self):
        return self.colorSection
    
    def setColorSection(self, colorSection):
        self.colorSection = colorSection

    def getColorSubSection(self):
        return self.colorSubSection
    
    def setColorSubSection(self, colorSubSection):
        self.colorSubSection = colorSubSection
    
