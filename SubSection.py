import Coordinate as co
from typing import List
import math
import random

class SubSection:

    points:List[co.Coordinate] = []
    generated_points_in_subsection:List[co.Coordinate] = []
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
    def __init__(self, section, r_index: float, phi_index: float): 

        self.generated_points_in_subsection = []

        self.phi_size = (section.phi_size / section.subsec_num_phi)

        self.start_phi = (section.phi_size * section.section_index)

        self.phi_index = phi_index
        self.phi_range = [self.start_phi + phi_index*self.phi_size, self.start_phi + (phi_index + 1)*self.phi_size]

        self.r_index = r_index
        self.r_base = section.max_r * math.sqrt(section.subsec_num_r) / section.subsec_num_r
        self.r_range = [math.sqrt(r_index)*self.r_base, math.sqrt(r_index + 1)*self.r_base]
        
        self.points = self.points_in_subsection(section)
        self.count = len(self.points)

    def points_in_subsection(self, section)->List[co.Coordinate]:
        
        subsection_points = [
            point for point in section.points
            if self.phi_range[0] <= point.getPhi() and point.getPhi() < self.phi_range[1] 
            and self.r_range[0] < point.getR() and point.getR() <= self.r_range[1]
        ]
        return subsection_points

    def generate_subsection_points(self, global_points_count, number_gen_points)->List:
        generated_points_number: int = int(round((self.count * number_gen_points)/global_points_count, 0))
        
        generated_points_subsection: List[co.Coordinate] = [[co.Coordinate(random.uniform(self.r_range[0], self.r_range[1]), random.uniform(self.phi_range[0], self.phi_range[1]), True)] for i in range(generated_points_number)]
        self.generated_points_in_subsection = generated_points_subsection
        return generated_points_subsection
        
    def concatenate_points_subsection(self, points: List[co.Coordinate]):
        self.points += points
        self.count = len(self.points)