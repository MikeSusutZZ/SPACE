import random
from menu import Menu

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

    def shipMenu(self, galaxy, col, row):
        def goIndMenu(args, shipIndex):
            self.indShipMenu(args, shipIndex)
        def unused(args, shipIndex):
            return not self.ships[shipIndex].used
        def getType(args, shipIndex):
            return self.ships[shipIndex].shipType
        shipMenu = Menu("Available Ships", "Which would you like to use?: ")
        shipMenu.addOptionalRepeatedItems(self.ships, goIndMenu, unused, getType)
        shipMenu.menu([[]], galaxy, col, row)

    def indShipMenu(self, args, shipIndex):
        galaxy = args[0]
        col = args[1]
        row = args[2]

        def doMove(arg):
            self.shipMovementMenu(galaxy, col, row, shipIndex)
        // ADD LOADING FUNC OPTIONALiTEMaDD BASED ON IF U HAVE FUEL, THEN IF ON PLANET
        def loadShip

        indMenu = Menu("What would you like to do with the chosen ship?", "Pick an action: ", inputType='let')
        keys = []
        actions = [doMove]

    def shipMovementMenu(self, galaxy, col, row, shipIndex):
        while True:
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
                        elif dir == 's':
                            tarShip.info()
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