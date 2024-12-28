import Coordinate as co
import random
from typing import List

class DataUtils:
    def max_radious(data_xy):
        max_object = max(data_xy, key=lambda data_xy: data_xy.getR())
        return max_object
    
    def setPhiShift(data_xy):
        co.Coordinate.shiftPhi = DataUtils.max_radious(data_xy).getPhi()
        return co.Coordinate.shiftPhi
    

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