import math
from typing import List
import Augmentation as au
import Coordinate as co
from icecream import ic
import matplotlib as plt

#subsections = max(1, int(math.sqrt((section_count / len(points)) * 100)))
class SectionGroup:
    def __init__(self, points:List[co.Coordinate], section_count:int):
        self.section_count = section_count
        self.points = points

class Section:

    points:List[co.Coordinate] = None
    section_index = 0
    max_r = 0
    count = 0
    subsec_num_r = 4
    subsec_num_phi = 4
    subsection_phi_size = 1
    phi_size = 0

    def __init__(self,  sectionGroup:SectionGroup, section_index:int):

        self.number_of_sections = sectionGroup.section_count
        self.section_index = section_index
        self.phi_size = 2 * math.pi / self.number_of_sections
        
        
        self.points = self.points_in_section(self.number_of_sections, sectionGroup.points, section_index)
        self.count = len(self.points)
        self.max_r = max(point.getR() for point in self.points) if self.points else 0


    def points_in_section(self, number_of_sections:int, points:List[co.Coordinate], section_index:int)->List[co.Coordinate]:
        
        section_points = [
            point for point in points
            if (section_index * self.phi_size) <= point.getPhi() and point.getPhi() < ((section_index + 1) * self.phi_size)
        ]
        
        return section_points
    
    

    

class SubSection:

    points:List[co.Coordinate] = None
    r_index = 0
    phi_index = 0
    phi_size = 0   
    phi_range = []
    r_range = []
    r_base = 0
    count = 0
    start_phi = 0


    #r_index - numer indeksu promienia
    #phi_index - numer indeksu kąta
    def __init__(self, section: Section, r_index: float, phi_index: float): 

        self.phi_size = (section.phi_size / section.subsec_num_phi)

        self.start_phi = (section.phi_size * section.section_index)

        self.phi_index = phi_index
        self.phi_range = [self.start_phi + phi_index*self.phi_size, self.start_phi + (phi_index + 1)*self.phi_size]

        self.r_index = r_index
        self.r_base = section.max_r * math.sqrt(section.subsec_num_r) / section.subsec_num_r
        self.r_range = [math.sqrt(r_index)*self.r_base, math.sqrt(r_index + 1)*self.r_base]
        
        self.points = self.points_in_subsection(section)
        self.count = len(self.points)

    def points_in_subsection(self, section: Section)->List[co.Coordinate]:
        
        subsection_points = [
            point for point in section.points
            if self.phi_range[0] <= point.getPhi() and point.getPhi() < self.phi_range[1] 
            and self.r_range[0] < point.getR() and point.getR() <= self.r_range[1]
        ]
        return subsection_points      



if __name__ == '__main__':
    points = au.x_train
    ic(len(points))
    # section = Section(points, 6, 0)
    # subsection = SubSection(section, 0, 0)
    # ic(section.count)
    # ic(subsection.count)
    # ic(subsection.points[0].getXY(), subsection.points[0].getR(), subsection.points[0].getPhi())
    # ic(section.max_r, section.phi_size)

    section_count = 6
    sectionGroup = SectionGroup(points, section_count)
    section = Section(sectionGroup, 1)
    subsection = SubSection(section, 3, 3)
    ic(section.count)
    ic(subsection.count)
    ic(subsection.points[0].getXY(), subsection.points[0].getR(), subsection.points[0].getPhi())
    ic(section.max_r, section.phi_size)

    ic(sum([sum([SubSection(section,i,j).count for i in range(4)]) for j in range(4)]))

    list = ([([SubSection(section,i,j).points for i in range(4)]) for j in range(4)])
    listSub = []
    for i in range(4):
        for j in range(4):
            if list[i][j] != []:
                for k in range(len(list[i][j])):
                    listSub.append(list[i][j][k].getR())
    
    list2 = section.points
    list3 = []
    for i in range(len(list2)):
        list3.append(list2[i].getR())

    def delete_duplicates_from_two_lists(list1, list2):
        for i in range(len(list1)):
            if list1[i] in list2:
                list2.remove(list1[i])
        return list2
    
    ic(delete_duplicates_from_two_lists(listSub, list3))
            