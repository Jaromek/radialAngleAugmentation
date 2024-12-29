import math
import Augmentation as au
from icecream import ic

class Section:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.name} ({self.start}-{self.end})'

    def __repr__(self):
        return str(self)

    def angle_size(n_angles):
        return 2 * math.pi / n_angles

    def points_in_and_stats(n_angles, points, section_num):
        size = Section.angle_size(n_angles)
        section_points = [
            point for point in points
            if section_num * size < point.getPhi() <= (section_num + 1) * size
        ]
        count = len(section_points)
        max_radius = max(point.getR() for point in section_points) if section_points else 0
        return section_points, count, max_radius

    def generate_points_distribution(n_angles, points, total_generated):
        total_points = len(points)
        ratios = [len(Section.points_in_and_stats(n_angles, points, num)[0]) / total_points for num in range(n_angles)]
        generated = [int(r * total_generated) for r in ratios]
        diff = total_generated - sum(generated)
        if diff > 0:
            min_idx = generated.index(min(generated))
            generated[min_idx] += diff
        return generated

class SubSection:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.name} ({self.start}-{self.end})'

    def __repr__(self):
        return str(self)

    def points_and_radius_list(n_angles, points, section_num):
        section_points, count, max_radius = Section.points_in_and_stats(n_angles, points, section_num)
        subsections = max(1, int(math.sqrt((count / len(points)) * 100)))
        subsection_angle = Section.angle_size(n_angles) / subsections
        radii = [max_radius * math.sqrt(i) / subsections for i in range(1, subsections + 1)]
        radii.insert(0, 0)
        return section_points, radii, subsection_angle
    

if __name__ == '__main__':
    n_angles = 5
    points = au.x_train

    for num in range(n_angles):
        section_points, radii, angle = SubSection.points_and_radius_list(n_angles, points, num)
        ic(num)
        ic(radii)
        ic(angle)

    ic(len(points))
    ic(Section.generate_points_distribution(n_angles, points, 10000))

    