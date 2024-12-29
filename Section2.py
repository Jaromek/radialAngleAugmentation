import math

class Section:
    def __init__(self, n_angles, points):
        self.n_angles = n_angles
        self.points = points
        self.section_angle_size = 2 * math.pi / n_angles

    def points_in_section(self, section_num):
        start_angle = section_num * self.section_angle_size
        end_angle = (section_num + 1) * self.section_angle_size
        return [p for p in self.points if start_angle <= p.getPhi() < end_angle]

    def elements_count_in_section(self, section_num):
        return len(self.points_in_section(section_num))

    def max_radius_in_section(self, section_num):
        points = self.points_in_section(section_num)
        return max((p.getR() for p in points), default=0)

    def generated_points_per_section(self, n_generated_points):
        total_points = len(self.points)
        ratios = [self.elements_count_in_section(i) / total_points for i in range(self.n_angles)]
        return [int(r * n_generated_points) for r in ratios]

    def adjust_generated_points(self, n_generated_points):
        generated_points = self.generated_points_per_section(n_generated_points)
        diff = n_generated_points - sum(generated_points)
        if diff > 0:
            min_idx = generated_points.index(min(generated_points))
            generated_points[min_idx] += diff
        return generated_points


class SubSection:
    def __init__(self, section):
        self.section = section

    def subsections_count(self, section_num):
        section_points = self.section.elements_count_in_section(section_num)
        total_points = len(self.section.points)
        return max(1, int(math.sqrt((section_points / total_points) * 100)))

    def equal_area_radii(self, section_num):
        section_radius = self.section.max_radius_in_section(section_num)
        subsections = self.subsections_count(section_num)
        return [section_radius * math.sqrt(i / subsections) for i in range(subsections + 1)]

    def points_in_subsection(self, section_num, subsection_num):
        subsection_size = self.section.section_angle_size / self.subsections_count(section_num)
        start_angle = section_num * self.section.section_angle_size + subsection_num * subsection_size
        end_angle = start_angle + subsection_size
        return [p for p in self.section.points_in_section(section_num) if start_angle <= p.getPhi() < end_angle]
