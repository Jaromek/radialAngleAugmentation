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

    

    def __init__(self, r_x: float, phi_y: float, polar = False, sectionID: int = 0, subsectionID: int = 0, global_subsectionID: int = 0, 
                 colorSection: tuple = (0,0,0), colorSubSection: tuple = (0,0,0), customColor: tuple = (1,0,0)):
        """
        Class constructor. Returns polar coordinates if polar = True, otherwise returns Cartesian coordinates
        """
        if polar:
            self.r = r_x
            self.phi = phi_y
        else:
            x = r_x
            y = phi_y
            self.setXY(x, y)
        
        self.sectionID = sectionID
        self.subsectionID = subsectionID

        self.colorSection = colorSection
        self.colorSubSection = colorSubSection
        self.customColor = customColor
        self.shiftPhi = 0
    

    def getXY(self):
        """
        Returns the Cartesian coordinates of the point x and y in the array -> [x, y]
        """
        x = self.r * math.cos(self.phi)
        y = self.r * math.sin(self.phi)       
        
        return [x, y]

    def setXY(self, x, y):
        """
        Sets the polar coordinates of the point based on the Cartesian coordinates x and y      
        """
        self.r = math.sqrt(x**2 + y**2)
        if self.r > 0:
            self.phi = math.acos(x/self.r)
        else:
            self.phi = 0 
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

    def setShiftPhi(self, shiftPhi):  
        self.shiftPhi = shiftPhi         

    def getShiftPhi(self):  
        return self.shiftPhi

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
    
