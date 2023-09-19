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
                return self.ships.pop(index)
            else: print("Didn't move")
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

    def moveShip(self, tarShip, galaxy, col, row):
        try:
            print(f"Trying to move the ship to {col}, {row}")
            galaxy.locations[row][col].shipArrives(tarShip)
            print(f"Moved the ship to {col}, {row}")
        except Exception as e:
            print(f"Unable to move that direction. Error: {e}\n")


    

    def menu(self, galaxy, col, row):
         while True:
            self.info()
            action = input("pick a ship you would like to move, or enter 'b' to go back: ").lower()
            if action == 'b': break
            else:
                tarShip = self.shipLeaves(int(action) - 1)
                print(tarShip)
                while True:
                    dir = input("Would you like to go? (u)p, (d)own (l)eft, (r)ight: ").lower()
                    if dir == 'u':
                        self.moveShip(tarShip, galaxy, col, row - 2)
                        break
                    elif dir == 'd':
                        self.moveShip(tarShip, galaxy, col + 1, row - 2)
                        break
                    elif dir == 'l':
                        self.moveShip(tarShip, galaxy, col - 1, row - 3)
                        break
                    elif dir == 'r':
                        self.moveShip(tarShip, galaxy, col - 1, row)
                        break
                    else:
                        print("Invalid input")
# sorted(self.ships, key=lambda x: x.used) 