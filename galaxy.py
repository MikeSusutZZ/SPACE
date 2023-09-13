import random
from location import Location
from planet import Planet
class Galaxy:
    def __init__(self, size):
        self.locations = [[0 for x in range(size)] for y in range(size)]

    def determineLoc():
        option = random.randint(1, 5)
        if option == 1 or option == 2:
            return Location(Planet())
        elif option == 3 or option == 4:
            return Location('empty')
        elif option == 5:
            return Location('asteriod')
        else:
            return 'Invalid option'

    