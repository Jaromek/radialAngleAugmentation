import math
import Coordinate as co
import GeometryUtils as gu
import DataUtils as du
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
        section_angle_size = gu.GeometryUtils.section_angle_size(n_angles)
        for section_num in range(n_angles):
            if point.getPhi() <= (section_num + 1)* section_angle_size:
                return section_num
    
    def points_in_section(n_angles, points, section_num):
        section_angle_size = gu.GeometryUtils.section_angle_size(n_angles)
        section = [point for point in points if section_num * section_angle_size < point.getPhi() < (section_num + 1) * section_angle_size]
        return section
    
    def number_of_elements_in_section(n_angles, points, section_num):
        return len(Section.points_in_section(n_angles, points, section_num))
    
    def section_radious(n_angles, points, section_num):
        section = Section.points_in_section(n_angles, points, section_num)
        return du.DataUtils.max_radious(section)


class SubSection:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
    
    def __str__(self):
        return f'{self.name} ({self.start}-{self.end})'
    
    def __repr__(self):
        return str(self)
    
    def subsections_number(n_angles, points, section_num):
        return abs(int(math.sqrt((Section.number_of_elements_in_section(n_angles, points, section_num)/len(points)) * 100))-2)

    def subsection_angle_size(n_angles, points, section_num):
        return gu.GeometryUtils.section_angle_size(n_angles) / SubSection.subsections_number(n_angles, points, section_num)
    


if __name__ == '__main__':
    
    n = 100
    tab = [co.Coordinate(random.uniform(-10, 10), random.uniform(-10, 10)) for i in range(100)]
    
    # print(len(tab))

    ic(Section.section_radious(5, tab, 2).getR())

    # for i in range(n):
        #ic(tab[i].getXY(),tab[i].getR(),tab[i].getPhi(), Section.point_section(5, tab[i]))

        # ic(SubSection.subsections_number(5, tab, Section.point_section(5, tab[i])))
        # ic(Section.point_section(5, tab[i]))

        
        # print(" ")