from SectionUtils import SectionGroup, Section, SubSection


def Augmentation(points, section_count, global_points_gen):
    
    """
    points - list of points
    section_count - number of sections
    global_points_gen - number of points to generate in whole data
    """

    sectionGroup = SectionGroup(points, section_count)
    sections = [Section(sectionGroup, i) for i in range(section_count)]
    generated_points = []

    for section in sections:
        subsections = [SubSection(section, i, j) for i in range(section.subsec_num_phi) for j in range(section.subsec_num_r)]

        for subsection in subsections:
            gen_pts = subsection.generate_subsection_points(sectionGroup.count, global_points_gen)
            subsection.concatenate_points_subsection(gen_pts)
            generated_points.extend(gen_pts)

        section.refresh_subsections(subsections)

    sectionGroup.refresh_sections(sections)

    return generated_points