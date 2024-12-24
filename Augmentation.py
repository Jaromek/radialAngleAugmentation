import Coordinate as co
import random

tab = []
for i in range(10):
    
    tab.append(co.Coordinate(random.randint(1, 10), random.randint(1, 10)))
    print(tab)

for i in range(10):
    print(tab[i].getXY())
    print(tab[i].getR())  
    print(tab[i].getPhi())  
 
class Augmentation():
    print("Augmentation")