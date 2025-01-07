import Section as sec
class GenerateData:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return self.data
    
    def generate_data():
        print("GenerateData.generate_data()")

        # def generate_points_distribution(self, sectionList: List[Section], num_phi_in_section, points, total_generated):
    #     total_points = len(points)
    #     ratios = [(section.count / (total_points)) for section in sectionList]
    #     generated = [int(ratio * total_generated) for ratio in ratios]
    #     diff = total_generated - sum(generated)
    #     if diff > 0:
    #         min_idx = generated.index(min(generated))
    #         generated[min_idx] += diff
    #     return generated