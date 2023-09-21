import random
from location import Location
from planet import Planet
from asteroids import Asteroid
class Galaxy:
    def __init__(self, size):
        self.locations = [[self.determineLoc() for x in range(size)] for y in range(size)]
        homeWorld = Planet()
        homeWorld.resources = {'C': 2, 'F': 2, 'M': 2, 'K': 0, 'D': 0}
        homeWorld.name = 'Home'
        homeWorld.used = False
        homeWorld.cargo.append('C')
        self.locations[size // 2][size // 2] = homeWorld

    def determineLoc(self):
        option = random.randint(1, 15)
        if option < 5:
            return Planet()
        elif option >= 5 and option < 12:
            return Location()
        elif option >= 12:
            return Asteroid()
        else:
            return 'Invalid option'
        
    def fullInfo(self):
        for i, row in enumerate(self.locations):
            # Print the row number and the corresponding letter 'A'
            
            
            for j, loc in enumerate(row):
                # Print the information for each location in the row
                print(f"{chr(j + 65)} {i + 1}:")
                loc.info()

        
    def info(self):
        print("      ", end='')
        for i, thing in enumerate(self.locations):
            print(f"( {chr(i + 65)} ) ", end='')
        print(f"\n")
        for i, row in enumerate(self.locations):
            print(f"( {i + 1} ) ", end='')
            for loc in row:
                act = '_'
                locType = '_'
                for ship in loc.ships:
                    if not ship.used:
                        act = '^'
                if isinstance(loc, Planet):
                    locType = 'P'
                elif isinstance(loc, Asteroid):
                    locType = 'A' 
                if isinstance(loc, Planet) and not loc.usage > 0:
                    act = '*'
                print(f"[{locType},{act}] ", end='')
            print("\n")

    def reactivate(self):
        for col in self.locations:
            for row in col:
                row.reactivate()
    

    