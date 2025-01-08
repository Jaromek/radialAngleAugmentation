from SectionUtils import SectionGroup, Section, SubSection
import DataUtils as du
from sklearn.datasets import make_blobs
from icecream import ic


n_angles = 5

x_train, y_train = make_blobs(n_samples=11000, centers=1, random_state=42, cluster_std=1.0)

x_train = du.DataUtils.normalize_data(x_train)

x_train = du.DataUtils.remove_outliers_lof(x_train)

x_train = du.DataUtils.shift_to_mass_center(x_train)

x_train = du.DataUtils.listed_class(x_train)

shifted_phi = du.DataUtils.setPhiShift(x_train)

max_r = du.DataUtils.max_radious_object(x_train).getPhi()


if __name__ == '__main__':
    points = x_train

    section_count = 7
    sectionGroup = SectionGroup(points, section_count)

    sections = [Section(sectionGroup, i) for i in range(section_count)]
       
    ic(sectionGroup.count)

    global_points_gen = 1000

    section_size_sum = 0

    for section in sections:
        subsections = [SubSection(section, i, j) for i in range(section.subsec_num_phi) for j in range(section.subsec_num_r)]

    
        for subsection in subsections:
            gen_pts = subsection.generate_subsection_points(sectionGroup.count, global_points_gen)
            subsection.concatenate_points_subsection(gen_pts)

        section.refresh_subsections(subsections)
        section_size_sum += section.count

    sectionGroup.refresh_sections(sections)
    
    ic(sectionGroup.count)