from section1_encapsulation import main_section_1
from section2_inheritance import main_section_2
from section3_polymorphism import main_section_3
from section4_repl import main_section_4

class Controller:
    def run(self):
        print("Welcome to the OOP Assignment!")
        main_section_1()
        main_section_2()
        main_section_3()
        main_section_4()
        print("All sections completed!")