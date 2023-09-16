import random
from location import Location
from planet import Planet
from asteroids import Asteroid
class Galaxy:
    def __init__(self, size):
        self.locations = [[self.determineLoc() for x in range(size)] for y in range(size)]

    def determineLoc(self):
        option = random.randint(1, 5)
        if option == 1 or option == 2:
            return Planet()
        elif option == 3 or option == 4:
            return Location()
        elif option == 5:
            return Asteroid()
        else:
            return 'Invalid option'
        

    