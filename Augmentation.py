from functools import reduce
import Coordinate as co
import random

tab = []
for i in range(3):
    
    tab.append(co.Coordinate(random.randint(1, 10), random.randint(1, 10)))
   

for i in range(3):
    print(tab[i].getXY(),tab[i].getR(),tab[i].getPhi())  
 
co.Coordinate.shiftPhi = 3.14/2

for i in range(3):
    print(tab[i].getXY(),tab[i].getR(),tab[i].getPhi()) 


class Augmentation():
    print("Augmentation")

print("-----------------")

# sec = list(filter(lambda x: x.getPhi() < 5.97 and x.getPhi() > 5.17, tab))

# for s in sec:
#     print(s.getXY(),s.getR(),s.getPhi()) 

def max_r(tab):
    max_object = max(tab, key=lambda tab: tab.getR())
    return max_object

# max_object = max(tab, key=lambda tab: tab.getR())


# print(max_object.getXY(),max_object.getR(),max_object.getPhi())


print(max_r(tab).getXY(),max_r(tab).getR(),max_r(tab).getPhi())

print("-----------------")
