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
        print("Ships at this location:")
        for i in range(0, len(self.ships)):
                print(f"{i + 1}) ", end='')
                self.ships[i].info()
                if i > 4:
                    print("")

    def info(self, col, row):
         print(f"{chr(col + 65)} {row}) ")
         print("Nothing here but empty space and whatever you brought with you")
         self.printShips()
         print('')

    def moveShip(self, tarShip, galaxy, col, row):
        try:
            #print(f"Trying to move the ship to {col}, {row}")
            galaxy.locations[row][col].shipArrives(tarShip)
            #print(f"Moved the ship to {col}, {row}")
        except Exception as e:
            print(f"Unable to move that direction. Error: {e}\n")

    def shipMovementMenu(self, galaxy, col, row):
        while True:
            self.info(col, row)
            action = input("pick a ship you would like to move, or enter 'x' to go back: ").lower()
            if action == 'x': break
            else:
                try:
                    tarShip = self.shipLeaves(int(action) - 1)
                    while True:
                        dir = input("Would you like to go? (u)p, (d)own (l)eft, (r)ight, view (g)alaxy, or 'x' to cancel: ").lower()
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
                        elif dir == 'g':
                            galaxy.info()
                        elif dir == 'x':
                            break
                        else:
                            print("Invalid input")
                except: print(f"No ship at index {action}")
    

    def menu(self, galaxy, col, row):
         self.shipMovementMenu(galaxy, col, row)
# sorted(self.ships, key=lambda x: x.used) 