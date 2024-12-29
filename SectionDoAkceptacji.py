import math
from typing import List
import Augmentation as au
import Coordinate as co
from icecream import ic
#subsections = max(1, int(math.sqrt((section_count / len(points)) * 100)))


class Section:

    points:List[co.Coordinate] = None
    n_angles = 0
    section_num = 0
    max_radious = 0
    count = 0
    subsections_number = 4

    def __init__(self,  points:List[co.Coordinate], n_angles:int, section_num:int):

        self.n_angles = n_angles
        self.points = self.points_in_section(n_angles, points, section_num)
        self.section_num = section_num

        count = len(self.points)
        max_radious = max(point.getR() for point in self.points) if self.points else 0


    def angle_size(self, n_angles):
        return 2 * math.pi / n_angles

    def points_in_section(self, n_angles:int, points:List[co.Coordinate], section_num:int)->List[co.Coordinate]:
        size = self.angle_size(n_angles)
        section_points = [
            point for point in points
            if (section_num * size) <= point.getPhi() and point.getPhi() < ((section_num + 1) * size)
        ]
        
        return section_points
    
    

    

class SubSection:

    points:List[co.Coordinate] = None
    r_i = 0
    phi_i = 0
    section_num = 0
    max_radious = 0
    #count = 0


    def __init__(self, section: Section, r_i, phi_i):

        self.phi_i = phi_i
        self.r_i = r_i
        self.max_radious = section.max_radious
        self.points = self.points_in_subsection(section, r_i, phi_i)
        


    def points_in_subsection(self, section: Section, r_i, phi_i):
        pass      

    def points_and_radius_list(section: Section):
        section_points = section.points
        section_count = section.count
        max_radious = section.max_radious




       
        # subsection_angle = Section.angle_size(n_angles) / subsections
        # radiouses = [max_radious * math.sqrt(i) / subsections for i in range(1, subsections + 1)]
        # radiouses.insert(0, 0)
        # return section_points, radiouses, subsection_angle
    


data = [co.Coordinate(1, 1), co.Coordinate(2, 2), co.Coordinate(3, 3), co.Coordinate(4, 4), co.Coordinate(5, 5), co.Coordinate(6, 6), co.Coordinate(7, 7), co.Coordinate(8, 8), co.Coordinate(9, 9), co.Coordinate(10, 10)]

sectionList:List[Section] = [Section(data, 4, 0), Section(data, 4, 1), Section(data, 4, 2), Section(data, 4, 3)]


def generate_points_distribution(self, sectionList: List[Section], n_angles, points, total_generated):
        total_points = len(points)
        ratios = [(section.count / (total_points)) for section in sectionList]
        generated = [int(ratio * total_generated) for ratio in ratios]
        diff = total_generated - sum(generated)
        if diff > 0:
            min_idx = generated.index(min(generated))
            generated[min_idx] += diff
        return generated














if __name__ == '__main__':
    n_angles = 4
    points = au.x_train

    for num in range(n_angles):
        section_points, radiouses, angle = SubSection.points_and_radius_list(n_angles, points, num)
        ic(num)
        ic(radiouses)
        ic(angle)

    ic(len(points))
    ic(Section.generate_points_distribution(n_angles, points, 10000))

    for num in range(n_angles):
        section_points, count, max_radious = Section.points_in_section_and_stats(n_angles, points, num)
        ic(num)
        ic(count)
        ic(max_radious)
        ic(len(section_points))

    

