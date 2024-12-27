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
    
    def list_of_elements_number_in_sections(n_angles, points):
        return [Section.number_of_elements_in_section(n_angles, points, section_num) for section_num in range(n_angles)]
    
    def occuracy_ratio_list(n_angles, points):
        return [Section.number_of_elements_in_section(n_angles, points, section_num)/len(points) for section_num in range(n_angles)]
    
    def number_of_generated_points_per_section(n_angles, points, n_generated_points):
        return [int(Section.occuracy_ratio_list(n_angles, points)[i] * n_generated_points) for i in range(n_angles)]
    
    def difference_between_generated_points(n_angles, points, n_generated_points):
        return n_generated_points - sum(Section.number_of_generated_points_per_section(n_angles, points, n_generated_points))
    
    def less_generated_points_list_index(n_angles, points, n_generated_points):
        if Section.difference_between_generated_points(n_angles, points, n_generated_points) > 0:
            return Section.number_of_generated_points_per_section(n_angles, points, n_generated_points).index(min(Section.number_of_generated_points_per_section(n_angles, points, n_generated_points)))
        else:
            return None
        
    def equalize_generated_points(n_angles, points, n_generated_points):
        index = Section.less_generated_points_list_index(n_angles, points, n_generated_points)
        if index != None:
            return [Section.number_of_generated_points_per_section(n_angles, points, n_generated_points)[i] + Section.difference_between_generated_points(n_angles, points, n_generated_points) if i == index else Section.number_of_generated_points_per_section(n_angles, points, n_generated_points)[i] for i in range(n_angles)]


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
        return int(math.sqrt((Section.number_of_elements_in_section(n_angles, points, section_num)/len(points)) * 100))
    
    def list_of_subsections_number_by_section(n_angles, points):
        return [SubSection.subsections_number_in_secton(n_angles, points, section_num) for section_num in range(n_angles)]

    def subsection_angle_size(n_angles, points, section_num):
        return gu.GeometryUtils.section_angle_size(n_angles) / SubSection.subsections_number(n_angles, points, section_num)   


if __name__ == '__main__':
    
    n = 100
    tab = [co.Coordinate(random.uniform(-10, 10), random.uniform(-10, 10)) for i in range(100)]
    
    # print(len(tab))

    ic(Section.section_radious(5, tab, 2).getR())

    ic(Section.list_of_number_of_elements_in_sections(5, tab))

    ic(Section.occuracy_ratio_list(5, tab))

    ic(sum(Section.occuracy_ratio_list(5, tab)))
    

    



    # for i in range(n):
        #ic(tab[i].getXY(),tab[i].getR(),tab[i].getPhi(), Section.point_section(5, tab[i]))

        # ic(SubSection.subsections_number(5, tab, Section.point_section(5, tab[i])))
        # ic(Section.point_section(5, tab[i]))

        
        # print(" ")