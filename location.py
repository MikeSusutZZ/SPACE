import random
from menu import Menu
from typing import TYPE_CHECKING

class Location:
    def __init__(self):
        self.ships = []

    def reactivate(self):
         for ship in self.ships:
              ship.reactivate()

    def shipArrives(self, ship):
        self.ships.append(ship)
    
    def shipLeaves(self, index, type):
        try:   
            ship = self.ships[index]
            if type == 1:
                if ship.moved():
                    return self.ships.pop(index)
                else: print("Didn't move")
            else:
                if ship.jumped():
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
            # col += 1
            # row -= 1
            print(f"Trying to move the ship to {col}, {row}")
            if ( not (row < 0 or row > 4 or col < 0 or col > 4)):
                galaxy.locations[row][col].shipArrives(tarShip)
            else: print(f"went over")
            #print(f"Moved the ship to {col}, {row}")
        except Exception as e:
            print(f"Unable to move that direction. Error: {e}\n")

    def shipMenu(self, galaxy, col, row):
        def goIndMenu(args, shipIndex):
            self.indShipMenu(args, shipIndex)
        def unused(args, shipIndex):
            return not self.ships[shipIndex].used
        def getType(args, shipIndex):
            return self.ships[shipIndex].infoStr()
        shipMenu = Menu("Available Ships", "Which would you like to use?: ")
        shipMenu.addOptionalRepeatedItems(self.ships, goIndMenu, unused, getType)
        shipMenu.menu([[]], galaxy, col, row)

    def indShipMenu(self, args, shipIndex):
        galaxy = args[0]
        col = args[1]
        row = args[2]

        def doMove(arg):
            self.shipMovementMenu(galaxy, col, row, shipIndex, 1)

        def doJump(arg):
            self.shipMovementMenu(galaxy, col, row, shipIndex, 2)

        def loadShip(arg):
            self.moveCargo(shipIndex, [], [])

        indMenu = Menu("What would you like to do with the chosen ship?", "Pick an action: ", inputType='let')
        keys = []
        from planet import Planet
        if isinstance(self, Planet):
            keys.append('onPlanet')
        if 'F' in self.ships[shipIndex].cargo:
            keys.append('canMove')
        if 'K' in self.ships[shipIndex].cargo:
            keys.append('canJump')
        actions = [doMove, loadShip]
        #print(f"Keys are {keys}")
        indMenu.addOptionalItems(['Load / Unload ship', 'Move', 'Jump'], [loadShip, doMove, doJump], ['onPlanet', 'canMove', 'canJump'])
        indMenu.menu([keys])

    def shipMovementMenu(self, galaxy, col, row, shipIndex, moveType):
                try:
                    tarShip = self.shipLeaves(shipIndex, moveType)
                    while True:
                        dir = input("Would you like to go? (u)p, (d)own (l)eft, (r)ight, view (g)alaxy, or 'x' to cancel: ").lower()
                        if dir == 'u':
                            self.moveShip(tarShip, galaxy, col, row - moveType)
                            break
                        elif dir == 'd':
                            self.moveShip(tarShip, galaxy, col, row + moveType)
                            break
                        elif dir == 'l':
                            self.moveShip(tarShip, galaxy, col - moveType, row)
                            break
                        elif dir == 'r':
                            self.moveShip(tarShip, galaxy, col + moveType, row)
                            break
                        elif dir == 's':
                            tarShip.info()
                        elif dir == 'g':
                            galaxy.info()
                        elif dir == 'x':
                            break
                        else:
                            print("Invalid input")
                except: print(f"No ship at index")
    
    # THIS NEEDS UPDATED LATER
    def menu(self, galaxy, col, row):
        sorted(self.ships, key=lambda x: x.shipType)
        self.info()
        self.shipMenu(galaxy, col, row)

            
             