import random

class Location:
    def __init__(self):
        self.ships = []


    def shipArrives(self, ship):
        self.ships.append(ship)
    
    def shipLeaves(self, index):
        ship = self.ships[index]
        if ship.moved():
            self.ships.pop(index)
        else: return False

    def printShips(self):
        print("Ships at this location")
        for i in range(0, len(self.ships)):
                print(f"{i + 1}) ", end='')
                self.ships[i].info()
                if i > 4:
                    print("")

    def menu(self):
         print()
# sorted(self.ships, key=lambda x: x.used) 