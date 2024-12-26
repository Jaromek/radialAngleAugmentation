import math
import Coordinate as co
import GeometryUtils as gu
import random
from icecream import ic

class Section:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.name} ({self.start}-{self.end})'

    def __repr__(self):
        return str(self)


    def point_section(n_angles, point):
        for section_num in range(1,n_angles+1):
            if point.getPhi() <= section_num * gu.GeometryUtils.section_angle_size(n_angles):
                return section_num
    
    def points_in_section(n_angles, tab):
        section = []
        for i in range(n_angles):
            section.append(list(filter(lambda x: x.getPhi() < (i+1)*gu.GeometryUtils.section_angle_size(n_angles) and x.getPhi() > i*gu.GeometryUtils.section_angle_size(n_angles), tab)))
        return section

if __name__ == '__main__':
    
    n = 5
    tab = [co.Coordinate(random.uniform(-10, 10), random.uniform(-10, 10)) for i in range(n)]
    for i in range(n):
        ic(tab[i].getXY(),tab[i].getR(),tab[i].getPhi(), Section.point_section(5, tab[i]))


    