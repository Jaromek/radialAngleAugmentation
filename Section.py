import math

class Section:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.name} ({self.start}-{self.end})'

    def __repr__(self):
        return str(self)

    def section_angle(n_angles):
        return 2*math.pi / n_angles

    # def which_section(self, n_angles):
    #     return next(angle for angle in range(n_angles) if self.phi < angle * Coordinate.section_angle(n_angles)) 