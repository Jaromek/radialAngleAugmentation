from __future__ import annotations
import Coordinate as co
from typing import List
from icecream import ic
import random
import math



class SectionGroup:

    points:List[co.Coordinate] = []
    count = 0
    section_count = 0
    generated_points_in_group:List[co.Coordinate] = []

    def __init__(self, points:List[co.Coordinate], section_count:int):
        self.section_count = section_count
        self.points = points
        self.count = len(self.points)
        self.generated_points_in_group = []

    def refresh_sections(self, sections_list):
        for section in sections_list:
            if section.generated_points_in_section != []:
                self.points += section.generated_points_in_section
                self.generated_points_in_group += section.generated_points_in_section
                section.generated_points_in_section = [] 

        self.count = len(self.points) 

class Section:

    points:List[co.Coordinate] = []
    generated_points_in_section:List[co.Coordinate] = []
    section_index = 0
    max_r = 0
    count = 0
    subsec_num_r = 4
    subsec_num_phi = 4
    subsection_phi_size = 1
    phi_size = 0

    def __init__(self,  sectionGroup:SectionGroup, section_index:int):


        

        self.generated_points_in_section = []
        self.number_of_sections = sectionGroup.section_count
        self.section_index = section_index
        self.phi_size = 2 * math.pi / self.number_of_sections
        
        
        self.points = self.points_in_section(self.number_of_sections, sectionGroup.points, section_index)
        self.count = len(self.points)
        self.max_r = max(point.getR() for point in self.points) if self.points else 0


    def points_in_section(self, number_of_sections:int, points:List[co.Coordinate], section_index:int)->List[co.Coordinate]:
        """
        Zwraca punkty z sekcji o indeksie section_index
        """
        
        section_points = [
            point for point in points
            if (section_index * self.phi_size) <= point.getPhi() and point.getPhi() < ((section_index + 1) * self.phi_size)
        ]
        
        for section_point in section_points:
            section_point.sectionID = section_index
            
        return section_points      
    
    def refresh_subsections(self, subsections_list: List[SubSection]):
        """
        Odświeża punkty w sekcji na podstawie punktów w podsekcjach
        """
        for subsection in subsections_list:
            if subsection.generated_points_in_subsection != []:
                self.points += subsection.generated_points_in_subsection
                self.generated_points_in_section += subsection.generated_points_in_subsection
                
                subsection.generated_points_in_subsection = []
                        
        self.count = len(self.points) 

    

class SubSection:

    points:List[co.Coordinate] = []
    generated_points_in_subsection:List[co.Coordinate] = []
    r_index = 0
    phi_index = 0
    phi_size = 0   
    phi_range = []
    r_range = []
    r_base = 0
    count = 0
    start_phi = 0
    subsection_index = 0
    


    #r_index - numer indeksu promienia
    #phi_index - numer indeksu kąta
    def __init__(self, section: Section, r_index: float, phi_index: float): 

        self.generated_points_in_subsection = []
        self.phi_size = (section.phi_size / section.subsec_num_phi)
        self.start_phi = (section.phi_size * section.section_index)

        

        self.phi_index = phi_index
        self.phi_range = [self.start_phi + phi_index*self.phi_size, self.start_phi + (phi_index + 1)*self.phi_size]

        self.r_index = r_index
        self.r_base = section.max_r * math.sqrt(section.subsec_num_r) / section.subsec_num_r
        self.r_range = [math.sqrt(r_index)*self.r_base, math.sqrt(r_index + 1)*self.r_base]

        self.subsection_index = r_index* section.subsec_num_phi + phi_index        
        
        self.points = self.points_in_subsection(section)
        self.count = len(self.points)

    def points_in_subsection(self, section: Section)->List[co.Coordinate]:
        """
        Zwraca punkty z podsekcji o zadanym zakresie kąta i promienia
        """
        
        subsection_points = [
            point for point in section.points
            if self.phi_range[0] <= point.getPhi() and point.getPhi() < self.phi_range[1] 
            and self.r_range[0] < point.getR() and point.getR() <= self.r_range[1]
        ]

        for subsection_point in subsection_points:
            subsection_point.subsectionID = self.subsection_index
            
        return subsection_points

    def generate_subsection_points(self, global_points_count: int, number_gen_points: int)->List:
        """
        Generuje punkty w podsekcji na podstawie liczby punktów w sekcji i liczby punktów globalnych
        """
        generated_points_number: int = int(round((self.count * number_gen_points)/global_points_count, 0))
        
        generated_points_subsection: List[co.Coordinate] = [co.Coordinate(random.uniform(self.r_range[0], self.r_range[1]), 
                                                                           random.uniform(self.phi_range[0], self.phi_range[1]), True)
                                                            for i in range(generated_points_number)]
        self.generated_points_in_subsection = generated_points_subsection
        return generated_points_subsection
        
    def concatenate_points_subsection(self, points: List[co.Coordinate]):
        """
        Dodaje punkty do podsekcji
        """
        self.points += points
        self.count = len(self.points)
                     
