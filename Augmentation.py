from SectionUtils import SectionGroup, Section, SubSection
import Coordinate as co


def Augmentation(points, section_count, global_points_gen):
    """
    points - list of points\n
    section_count - number of sections\n
    global_points_gen - number of points to generate in whole data
    """



    sectionGroup = SectionGroup(points, section_count)
    sections = [Section(sectionGroup, i) for i in range(section_count)]
    for section in sections:
        subsections = [SubSection(section, i, j) for i in range(section.subsec_num_phi) for j in range(section.subsec_num_r)]


        for subsection in subsections:
            gen_pts = subsection.generate_subsection_points(sectionGroup.count, global_points_gen)
            subsection.concatenate_points_subsection(gen_pts)

        section.refresh_subsections(subsections)

    sectionGroup.refresh_sections(sections)




# if __name__ == '__main__':
    # points = x_train

    # section_count = 7
    # sectionGroup = SectionGroup(points, section_count)

    # sections = [Section(sectionGroup, i) for i in range(section_count)]

    # global_points_gen = 1000

    # section_size_sum = 0

    # for section in sections:
    #     subsections = [SubSection(section, i, j) for i in range(section.subsec_num_phi) for j in range(section.subsec_num_r)]

    
    #     for subsection in subsections:
    #         gen_pts = subsection.generate_subsection_points(sectionGroup.count, global_points_gen)
    #         subsection.concatenate_points_subsection(gen_pts)

    #     section.refresh_subsections(subsections)
    #     section_size_sum += section.count

    # sectionGroup.refresh_sections(sections)

    # du.co.Coordinate.shiftPhi = 0
    
    # ic(sectionGroup.count)