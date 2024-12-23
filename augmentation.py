import numpy as np

class Augmentacja:
    def __init__(self, points):
            
        self.x = np.array(points[:][0])
        self.y = np.array(points[:][1])
        self.n_points = len(self.x)
        
    def get_points(self):
        return self.x, self.y
        
    def get_points_as_tuples(self):
        return list(zip(self.x, self.y))