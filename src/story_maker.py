import random as rd


class Story:

    seed = 0
    intro = ""
    first_midpoint = ""
    second_midpoint = ""
    character_a = ""
    character_b = ""
    need = ""
    ending = ""

    def __init__(self, seed):
        self.seed = seed
        self.create_intro()
        self.create_first_midpoint()
        self.create_second_midpoint()
        self.create_character_a()
        self.create_character_b()
        self.create_need()
        self.create_ending()

    def create_intro(self):
        pass

    def create_first_midpoint(self):
        with open("../data/Veale_db/Veale_s script midpoints.xlsx") as f:
            print(f)

    def create_second_midpoint(self):
        pass

    def create_character_a(self):
        pass

    def create_character_b(self):
        pass

    def create_need(self):
        pass

    def create_ending(self):
        pass

    def return_story(self):
        full_story = ""


story = Story(0)
