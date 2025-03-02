import numpy as np

a = [1,3,4,5,6,7,8,9,10]
b = [3,5,7,9,11,13,15,17,19]

c = np.concatenate((a,b), axis=0)
print(c[1:])