import random
from planet import Planet

class Location:
    def __init__(self, has):
        self.has = has
        self.ships = []


    def shipArrives(self, ship):
        self.ships.append(ship)
    
    def shipLeaves(self, index):
        ship = self.ships[index]
        if ship.moved():
            self.ships.remove(index)
        else: return False

    def info(self):
        if(self.has == 'empty'):
            print("No planets in the sector")
        elif self.has == 'asteroid':
            print('This sector is full of dangerously sized asteroids')
            print('There is nothing worth dying for out here')
        elif isinstance(self.has, Planet):
            self.has.info()
        print("Ships at this location")
        for i in range(0, len(self.ships)):
                print(f"{i}) ", end='')
                self.ships[i].info()
                if i > 4:
                    print("")

# sorted(self.ships, key=lambda x: x.used)