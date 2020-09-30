import os
from random import choice


class Names:
    def __init__(self):
        self.male_names = []
        self.female_names = []
        female = os.path.dirname(__file__) + r"/Names/Female.txt"
        male = os.path.dirname(__file__) + r"/Names/Female.txt"
        with open(male, "r") as file:
            for line in file.readlines():
                self.male_names.append(line.strip())

        with open(female, "r") as file:
            for line in file.readlines():
                self.female_names.append(line.strip())
        # print(self.male_names)
        # print(self.female_names)

    def get_random_name(self):
        names = [self.male_names, self.female_names]
        return choice(choice(names))



#
# name = Names()
#
# print(name.get_random_name())
