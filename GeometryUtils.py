import math
import Coordinate as co

class GeometryUtils:

    def section_angle_size(n_angles):
        return 2*math.pi / n_angles
    
    def is_in_radious(point_radious, start_radious, end_radious):
        return start_radious <= point_radious <= end_radious

    def is_in_angle(point_angle, angle_start, angle_end):
        return angle_start <= point_angle <= angle_end


    def radious_of_equal_areas(section_radious, subsections_count):
        subsections_count = math.sqrt(subsections_count)
        radiouses_of_section = []

        smallest_r = section_radious * math.sqrt(subsections_count) / subsections_count
        radiouses_of_section.append(smallest_r)

        for i in range(2, subsections_count + 1):
            radious_i = smallest_r * math.sqrt(i)
            radiouses_of_section.append(radious_i)
        radiouses_of_section.insert(0, 0)

        return radiouses_of_section
    
    
    
    

    
