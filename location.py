import random

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
        else:
            self.has.info()
        print("Ships at this location")
        for i in range(0, len(self.ships)):
                print(f"{i + 1}) ", end='')
                self.ships[i].info()
                if i > 4:
                    print("")

# sorted(self.ships, key=lambda x: x.used)