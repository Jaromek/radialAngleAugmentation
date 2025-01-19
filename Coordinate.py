import math

class Coordinate:

    r: float = 1
    phi: float = 0
    shiftPhi: float = 0
    sectionID: int = 0
    subsectionID: int = 0
    global_subsectionID: int = 0
    colorSection: tuple = (0,0,0)
    colorSubSection: tuple = (0,0,0)
    customColor: tuple = (0,0,0)

    

    def __init__(self, r: float, phi: float, polar = False, sectionID: int = 0, subsectionID: int = 0, global_subsectionID: int = 0, 
                 colorSection: tuple = (0,0,0), colorSubSection: tuple = (0,0,0), customColor: tuple = (1,0,0)):
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

        self.colorSection = colorSection
        self.colorSubSection = colorSubSection
        self.customColor = customColor
    

    def getXY(self):
        """
        zwraca współrzędne kartezjańskie punktu x i y w tablicy -> [x, y]
        """
        x = self.r * math.cos(self.phi - Coordinate.shiftPhi if self.phi - Coordinate.shiftPhi >= 0 else self.phi - Coordinate.shiftPhi + 2*math.pi)
        y = self.r * math.sin(self.phi - Coordinate.shiftPhi if self.phi - Coordinate.shiftPhi >= 0 else self.phi - Coordinate.shiftPhi + 2*math.pi)

        # x = self.r * math.cos(self.phi if self.phi >= 0 else self.phi + 2*math.pi)
        # y = self.r * math.sin(self.phi if self.phi >= 0 else self.phi + 2*math.pi)
        
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
        #return self.phi - Coordinate.shiftPhi if self.phi - Coordinate.shiftPhi >= 0 else self.phi - Coordinate.shiftPhi + 2*math.pi
        return self.phi

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

    def getCustomColor(self):
        return self.customColor
    
    def setCustomColor(self, customColor):
        self.customColor = customColor
    
