import Coordinate as co
import random

class DataUtils:
    def max_r(tab):
        max_object = max(tab, key=lambda tab: tab.getR())
        return max_object
    
    def setPhiShift(max_r):
        co.Coordinate.shiftPhi = max_r.getPhi()
        return co.Coordinate.shiftPhi
    

if __name__ == '__main__':
    tab = []

    n = 10

    for i in range(n):
        tab.append(co.Coordinate(random.randint(1, 10), random.randint(1, 10)))

    print("-----------------")

    for i in range(n):
        print(tab[i].getXY(),tab[i].getR(),tab[i].getPhi())
    
    print("-----------------")

    max_r = DataUtils.max_r(tab)

    print(max_r.getXY(),max_r.getR(),max_r.getPhi())

    print("-----------------")

    DataUtils.setPhiShift(DataUtils.max_r(tab))

    print(co.Coordinate.shiftPhi)

    print("-----------------")

    for i in range(n):
        print(tab[i].getXY(),tab[i].getR(),tab[i].getPhi())

    print("-----------------")

    print(max_r.getXY(),max_r.getR(),max_r.getPhi())