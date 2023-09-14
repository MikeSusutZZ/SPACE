from location import Location
import random

class Asteroid(Location):
    def __init__(self):
        super().__init__()

    def info(self):
        print("Asteroid field")
        self.printShips()

    def reactivate(self):
        for ship in self.ships:
            if random.randint(1,2) == 1:
                self.ships.remove(ship)