import random

class Location:
    def __init__(self):
        self.ships = []

    def reactivate(self):
         for ship in self.ships:
              ship.reactivate()

    def shipArrives(self, ship):
        self.ships.append(ship)
    
    def shipLeaves(self, index):
        try:   
            ship = self.ships[index]
            if ship.moved():
                self.ships.pop(index)
        except: 
            print("There was no ship at that index")
                

    def printShips(self):
        print("Ships at this location")
        for i in range(0, len(self.ships)):
                print(f"{i + 1}) ", end='')
                self.ships[i].info()
                if i > 4:
                    print("")

    def info(self):
         print("Nothing but here but empty space and whtever you brought with you")
         self.printShips()

    

    def menu(self):
         while True:
            self.info()
            action = input("pick a ship you would like to move, or enter 'b' to go back: ").lower()
            if action == 'b': break
            else:
                tarShip = self.shipLeaves
# sorted(self.ships, key=lambda x: x.used) 