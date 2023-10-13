from location import Location
import random
from menu import BTElement

class Asteroid(Location):
    def __init__(self):
        super().__init__()

    def info(self, col, row):
        print(f"{chr(col + 65)} {row}) ")
        print("Asteroid field")
        self.printShips()
        print('')

    def infoBTE(self, col, row):
        title = (f"{chr(col + 65)} {row}) ")
        title += ("Asteroid field")
        text = self.textShips()
        return BTElement(title, text)

    def reactivate(self):
        super().reactivate
        for ship in self.ships:
            if random.randint(1,2) == 1:
                self.ships.remove(ship)