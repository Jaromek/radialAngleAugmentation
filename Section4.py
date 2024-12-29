import math
from typing import List
import Coordinate as co
import Augmentation as au
import DataUtils as du

class Section:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.name} ({self.start}-{self.end})'
    
    def __repr__(self):
        return str(self)
    
    def angle_size(n_angles):
        return 2 * math.pi / n_angles
    
    def point_section(n_angles, point):
        section_angle_size = Section.angle_size(n_angles)
        for section_num in range(n_angles):
            if point.getPhi() <= (section_num + 1) * section_angle_size:
                return section_num

    def points_in_section(n_angles, points:List[co.Coordinate], section_num):
        section_angle_size = Section.angle_size(n_angles)
        section = [point for point in points if section_num * section_angle_size <= point.getPhi() < (section_num + 1) * section_angle_size]
        return section
    
    def max_radious_from_section(n_angles, points, section_num):
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

        def subsections_number_in_secton(n_angles, points, section_num):
            number_of_elements_in_section = len(Section.points_in_section(n_angles, points, section_num))
            return int(math.sqrt(number_of_elements_in_section/len(points) * 100))