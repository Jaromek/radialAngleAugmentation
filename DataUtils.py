import Coordinate as co
import random
from typing import List
import math

class DataUtils:
    section_angle_number = 1

    def __init__(self , section_angle_number:int):
        self.section_angle_number = section_angle_number
        
    def max_radious_object(data_xy):
        max_object = max(data_xy, key=lambda data_xy: data_xy.getR())
        return max_object
    
    def setPhiShift(data_xy):
        co.Coordinate.shiftPhi = DataUtils.max_radious_object(data_xy).getPhi()
        return co.Coordinate.shiftPhi
    
    # def generate_points_distribution(self, sectionList: List[Section], num_phi_in_section, points, total_generated):
    #     total_points = len(points)
    #     ratios = [(section.count / (total_points)) for section in sectionList]
    #     generated = [int(ratio * total_generated) for ratio in ratios]
    #     diff = total_generated - sum(generated)
    #     if diff > 0:
    #         min_idx = generated.index(min(generated))
    #         generated[min_idx] += diff
    #     return generated

    

if __name__ == '__main__':
    tab:List[co.Coordinate] = []

    n = 10

    for i in range(n):
        tab.append(co.Coordinate(random.randint(1, 10), random.randint(1, 10)))

    print("-----------------")

    for i in range(n):
        print(tab[i].getXY() ,tab[i].getR(),tab[i].getPhi())
    
    print("-----------------")

    max_r = DataUtils.max_radious(tab)

    print(max_r.getXY(),max_r.getR(),max_r.getPhi())

    print("-----------------")

    DataUtils.setPhiShift(DataUtils.max_r(tab))

    print(co.Coordinate.shiftPhi)

    print("-----------------")

    for i in range(n):
        print(tab[i].getXY(),tab[i].getR(),tab[i].getPhi())

    print("-----------------")

    print(max_r.getXY(),max_r.getR(),max_r.getPhi())