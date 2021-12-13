import random as rd
from openpyxl import load_workbook


# The story class holds all function needed to create a story,
# The seed given at creation will be used in the random elements of the story
class Story:

    # These variables store the different story elements
    intro = ""
    first_midpoint = []
    second_midpoint = []
    character_a = ("", "")
    character_b = ("", "")
    need = ""
    ending = ""

    def __init__(self, seed):
        rd.seed(seed)

        self.create_intro()
        self.create_second_midpoint()
        self.create_first_midpoint()
        self.create_character_a()
        self.create_character_b()
        self.create_need()
        self.create_ending()

        self.return_story()

    # This function creates the introduction of the story
    def create_intro(self):
        self.intro = "Once upon a time,"

    # This function creates the first midpoint of the story: a truple of verbs
    def create_second_midpoint(self):
        # Open the "Script midpoints" sheet
        workbook = load_workbook(filename="../data/Veale_db/Veale_s script midpoints.xlsx")
        work_sheet = workbook.active

        # Choose a random row in the worksheet
        random_index = rd.randint(2, 2761)

        # Store the first verb in the row
        midpoint = [work_sheet[random_index][0].value]

        # Choose a random one of the second verbs in the row
        verb2 = work_sheet[random_index][1].value.split(", ")
        midpoint.append(rd.choice(verb2))

        # Choose a random one of the third verbs in the row
        verb3 = work_sheet[random_index][2].value.split(", ")
        midpoint.append(rd.choice(verb3))

        # Store the first midpoint
        self.second_midpoint = midpoint

    # This function creates the second midpoint of the story, a truple of verbs, based upon the first midpoint
    def create_first_midpoint(self):
        # Open the "Script midpoints" sheet
        workbook = load_workbook(filename="../data/Veale_db/Veale_s script midpoints.xlsx")
        work_sheet = workbook.active

        # Retrieve the last verb of the first midpoint
        ending_verb = self.second_midpoint[0]

        # Find all the options for rows starting with the verb
        options = []
        for row in range(2, 2761):
            if ending_verb in work_sheet[row][2].value.split(", "):
                options.append(row)

        # If there is an option
        if len(options) != 0:
            # Choose a random one of these rows
            row = rd.choice(options)

            # Store the first verb in the row
            midpoint = [work_sheet[row][0].value]

            # Choose a random one of the second verbs in the row
            verb2 = work_sheet[row][1].value.split(", ")
            midpoint.append(rd.choice(verb2))

            # Choose a random one of the third verbs in the row
            verb3 = work_sheet[row][2].value.split(", ")
            midpoint.append(rd.choice(verb3))

            # Store the second midpoint
            self.first_midpoint = midpoint
        else:
            print("No second midpoint: starting over")

    # This function creates a character A and a trait based upon the first midpoint, as a subject
    def create_character_a(self):
        # Open the "Category actions" sheet
        workbook = load_workbook(filename="../data/results/extracted_category_actions.xlsx")
        work_sheet = workbook.active

        # Retrieve the midpoint verbs from the first midpoint
        midpoint_options = self.first_midpoint.copy()
        options = []

        # Until a character is found or until we are out of verbs
        while len(options) < 1 and len(midpoint_options) > 0:
            # Pick one of the remaining verbs
            verb = rd.choice(midpoint_options)

            # Remove it from the possible options
            midpoint_options.remove(verb)

            # Find the rows that contain the verb
            options = []
            for row in range(1, 162):
                if work_sheet[row][2].value is not None:
                    if verb in work_sheet[row][2].value.split(", "):
                        options.append(row)

        # If no possible options were found
        if len(options) < 1:
            print("No character found: taking a default one")
            character = "prince"
        else:
            # Choose a random one of the possible character options
            character = work_sheet[rd.choice(options)][1].value.lower()

        # Open the "Quality inventory" sheet
        workbook = load_workbook(filename="../data/Veale_db/Veale_s quality inventory.xlsx")
        work_sheet = workbook.active

        # Retrieve the midpoint verbs from the first midpoint
        midpoint_options = self.first_midpoint.copy()
        options = []

        # Until a trait is found or until we are out of verbs
        while len(options) < 1 and len(midpoint_options) > 0:
            # Pick one of the remaining verbs
            verb = rd.choice(midpoint_options)

            # Remove it from the possible options
            midpoint_options.remove(verb)

            # Find the rows that contain the verb
            options = []
            for row in range(1, 1973):
                if work_sheet[row][2].value is not None:
                    if verb in work_sheet[row][2].value.split(", "):
                        options.append(row)

        # If no possible options were found
        if len(options) < 1:
            print("No trait found: taking a default one")
            trait = "humble"
        else:
            # Choose a random one of the possible trait options
            trait = work_sheet[rd.choice(options)][0].value

        # Store the character and trait
        self.character_a = (character, trait)

    # This function creates a character B and a trait based upon the first midpoint, as an object
    def create_character_b(self):
        # Open the "Category actions" sheet
        workbook = load_workbook(filename="../data/results/extracted_category_actions.xlsx")
        work_sheet = workbook.active

        # Retrieve the midpoint verbs from the first midpoint
        midpoint_options = self.first_midpoint.copy()
        options = []

        # Until a character is found or until we are out of verbs
        while len(options) < 1 and len(midpoint_options) > 0:
            # Pick one of the remaining verbs
            verb = rd.choice(midpoint_options)

            # Remove it from the possible options
            midpoint_options.remove(verb)

            # Find the rows that contain the verb
            options = []
            for row in range(1, 162):
                if work_sheet[row][3].value is not None:
                    if verb in work_sheet[row][3].value.split(", "):
                        options.append(row)

        # If no possible options were found
        if len(options) < 1:
            print("No character found: taking a default one")
            character = "princess"
        else:
            # Choose a random one of the possible character options
            character = work_sheet[rd.choice(options)][1].value.lower()

        # Open the "Quality inventory" sheet
        workbook = load_workbook(filename="../data/Veale_db/Veale_s quality inventory.xlsx")
        work_sheet = workbook.active

        # Retrieve the midpoint verbs from the first midpoint
        midpoint_options = self.first_midpoint.copy()
        options = []

        # Until a trait is found or until we are out of verbs
        while len(options) < 1 and len(midpoint_options) > 0:
            # Pick one of the remaining verbs
            verb = rd.choice(midpoint_options)

            # Remove it from the possible options
            midpoint_options.remove(verb)

            # Find the rows that contain the verb
            options = []
            for row in range(1, 1973):
                if work_sheet[row][3].value is not None:
                    if verb in work_sheet[row][3].value.split(", "):
                        options.append(row)

        # If no possible options were found
        if len(options) < 1:
            print("No trait found: taking a default one")
            trait = "smart"
        else:
            # Choose a random one of the possible trait options
            trait = work_sheet[rd.choice(options)][0].value

        # Store the character and trait
        self.character_b = (character, trait)

    # This function creates a need for character A based on the midpoints.
    def create_need(self):
        # But it does not do anything yet
        pass

    # This function generates an ending based on the second midpoint
    def create_ending(self):
        # Open the "Closing bookend actions" sheet
        workbook = load_workbook(filename="../data/Veale_db/Veale_s closing bookend actions.xlsx")
        work_sheet = workbook.active

        # Retrieve the last verb of the second midpoint
        verb = self.second_midpoint[2]

        # Find the row in which this verb resides and pick one of the options of closing actions.
        for row in range(1, 244):
            if work_sheet[row][0].value == verb:
                self.ending = rd.choice(work_sheet[row][2].value.split(", "))

        # If no row was found using the verb
        if self.ending == "":
            print("No bookend found: taking standard one")
            self.ending = "And they lived happily ever after!"

    # This function prints the story in a readable format.
    def return_story(self):
        # Start sentence
        print(self.intro, "there was a " + self.character_a[1], self.character_a[0])
        # Introduction of character B
        print("They knew a", self.character_b[0], "that was", self.character_b[1])
        # First midpoint idiomatized
        for verb in self.first_midpoint:
            print(self.util_idiomatize(verb).replace("A", "the " + self.character_a[0])
                  .replace("B", "the " + self.character_b[0]))
        # Second midpoint idiomatized
        for verb in self.second_midpoint[1:]:
            print(self.util_idiomatize(verb).replace("A", "the " + self.character_a[0])
                  .replace("B", "the " + self.character_b[0]))
        # Ending
        print(self.ending.replace("A ", "the " + self.character_a[0])
                  .replace("B ", "the " + self.character_b[0]))

    # This function returns the idiomatized version of the input verb
    @staticmethod
    def util_idiomatize(verb):
        # Open the "Idiomatic actions" sheet
        workbook = load_workbook(filename="../data/Veale_db/Veale_s idiomatic actions.xlsx")
        work_sheet = workbook.active

        # If the verb is reversed
        if verb[0] == "*":
            verb = verb[1:]
            # Find the row with the verb and return a random idiomatized version from it
            for row in range(2, 820):
                if work_sheet[row][0].value == verb:
                    # Reverse the characters
                    return rd.choice(work_sheet[row][4].value.split(", "))\
                        .replace("A", "C")\
                        .replace("B", "A")\
                        .replace("C", "B")
        else:
            # Find the row with the verb and return a random idiomatized version from it
            for row in range(2, 820):
                if work_sheet[row][0].value == verb:
                    return rd.choice(work_sheet[row][4].value.split(", "))

        # If none are found
        return verb


story = Story(5)

# 32 no first character
