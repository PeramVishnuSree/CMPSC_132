# Object oriented programming practice part1
# create the class Person that stores information about a person (name and date of birth)
# and provides age based on birthday

import datetime
class Person:

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    # you can use the @property method to compute age() as an attribute
    def age(self):
        today = datetime.date.today()
        month, day, year = self.birthdate.split('/')
        age = today.year - int(year)

        if today < datetime.date(today.year, int(month), int(day)):
            age -= 1

        return age
