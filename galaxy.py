import random
from location import Location
from planet import Planet
from asteroids import Asteroid
class Galaxy:
    def __init__(self, size):
        self.locations = [[0 for x in range(size)] for y in range(size)]
        self.size = size

    def determineLoc():
        option = random.randint(1, 5)
        if option == 1 or option == 2:
            return Planet()
        elif option == 3 or option == 4:
            return Location()
        elif option == 5:
            return Asteroid()
        else:
            return 'Invalid option'
        
    def info(self):
        for row in self.locations:
            for loc in row:
                act = '_'
                locType = '_'
                for ship in loc.ships:
                    if isinstance(loc, Planet) and not ship.used:
                        act = '^'
                if isinstance(loc, Planet):
                    locType = 'P'
                elif isinstance(loc, Asteroid):
                    locType = 'A' 
                if isinstance(loc, Planet) and not loc.used:
                    act = '*'
                print(f"[{locType},{act}]", end='')
            print("")

        

    