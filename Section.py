import math
from typing import List
import Augmentation as au
import Coordinate as co
from icecream import ic
from SubSection import SubSection



class SectionGroup:

    points:List[co.Coordinate] = []
    count = 0
    section_count = 0
    generated_points_in_group:List[co.Coordinate] = []

    def __init__(self, points:List[co.Coordinate], section_count:int):
        self.section_count = section_count
        self.points = points
        self.count = len(self.points)
        self.generated_points_in_group = []

    def refresh_sections(self, sections_list):
        for section in sections_list:
            if section.generated_points_in_section != []:
                self.points += section.generated_points_in_section
                self.generated_points_in_group += section.generated_points_in_section
                ic(len(section.generated_points_in_section))
                section.generated_points_in_section = [] 

        self.count = len(self.points) 


class Section:

    points:List[co.Coordinate] = []
    generated_points_in_section:List[co.Coordinate] = []
    section_index = 0
    max_r = 0
    count = 0
    subsec_num_r = 4
    subsec_num_phi = 4
    subsection_phi_size = 1
    phi_size = 0

    def __init__(self,  sectionGroup:SectionGroup, section_index:int):

        self.generated_points_in_section = []
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
    
    def refresh_subsections(self, subsections_list: List[SubSection]):
        for subsection in subsections_list:
            if subsection.generated_points_in_subsection != []:
                self.points += subsection.generated_points_in_subsection
                self.generated_points_in_section += subsection.generated_points_in_subsection
                
                subsection.generated_points_in_subsection = []
                  

        ic(len(self.generated_points_in_section))       
        self.count = len(self.points) 
                     



if __name__ == '__main__':
    points = au.x_train

    section_count = 7
    sectionGroup = SectionGroup(points, section_count)

    sections = [Section(sectionGroup, i) for i in range(section_count)]
       
    ic(sectionGroup.count)

    global_points_gen = 1000

    section_size_sum = 0

    for section in sections:
        subsections = [SubSection(section, i, j) for i in range(section.subsec_num_phi) for j in range(section.subsec_num_r)]

    
        for subsection in subsections:
            gen_pts = subsection.generate_subsection_points(sectionGroup.count, global_points_gen)
            subsection.concatenate_points_subsection(gen_pts)

        section.refresh_subsections(subsections)
        section_size_sum += section.count

    sectionGroup.refresh_sections(sections)
    ic(section_size_sum)
    ic(sectionGroup.count)

        
    



    # sum = 0
    # gen_sum = 0
    # for i in range(4):
    #     for j in range(4):
    #         subsection_ = SubSection(section, i, j)
    #         sum += subsection_.count
    #         gen_points = subsection_.generate_subsection_points(len(points), number_gen_points)
    #         ic(subsection_.count)
    #         ic(len(gen_points))
    #         subsection_.concatenate_points_subsection(gen_points)

    #         ic(subsection_.count)


    


    # ic(section.count)

    # ic(len(points))
    
    # ic(sum)
    # ic(gen_sum)



    # gen_points = subsection.generate_subsection_points(len(points), number_gen_points)
    # ic(len(gen_points))
    # ic(sectionGroup.count)
    # ic(section.count)
    # ic(subsection.count)
    # ic(subsection.points[0].getXY(), subsection.points[0].getR(), subsection.points[0].getPhi())
    # ic(section.max_r, section.phi_size)

    # ic(sum([sum([SubSection(section,i,j).count for i in range(4)]) for j in range(4)]))

    # list = ([([SubSection(section,i,j).points for i in range(4)]) for j in range(4)])
    # listSub = []
    # for i in range(4):
    #     for j in range(4):
    #         if list[i][j] != []:
    #             for k in range(len(list[i][j])):
    #                 listSub.append(list[i][j][k].getR())
    
    # list2 = section.points
    # list3 = []
    # for i in range(len(list2)):
    #     list3.append(list2[i].getR())

    # def delete_duplicates_from_two_lists(list1, list2):
    #     for i in range(len(list1)):
    #         if list1[i] in list2:
    #             list2.remove(list1[i])
    #     return list2
    
    # ic(delete_duplicates_from_two_lists(listSub, list3))

    # ic(subsection.generate_subsection_points)
            