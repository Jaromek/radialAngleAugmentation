import Coordinate as co
import random
# class Augmentation():
tab = []
for i in range(10):
    
    tab.append(co.Coordinate(random.randint(1, 10), random.randint(1, 10)))


for i in range(10):
    print(tab[i].getXY())
    print(tab[i].getR())  
    print(tab[i].getPhi())   