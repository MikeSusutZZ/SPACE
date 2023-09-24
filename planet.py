from location import Location
import random
import costs
from menu import Menu
from shipYard import ShipYard

class Planet(Location):
    
    def __init__(self):
        super().__init__()
        self.resources = {"C": self.genResources('C'), "F": self.genResources('F'),
                            "M": self.genResources('M'), "K": self.genResources('K')}
        self.name = genName()
        self.cargo = []
        self.usage = 0
        self.upgraded = False

        self.civLevel = 0
        self.shipYard = ShipYard(self)

    def menu(self, galaxy, col, row):

        def shipMove(arg):
            super(Planet, self).shipMovementMenu(arg[0], arg[1], arg[2])
        def shipLoading(arg):
            self.loadingMenu(arg[1], arg[2])
        def buildShip(arg):
            self.shipYard.menu(self)
        def buildStructure(arg):
            self.buildMenu()
        def doHarvest(arg):
            self.harvest()
        def doInfo(arg):
            self.info(arg[1], arg[2])
        while True:
            keys = []
            if len(self.ships) > 0: keys.append('hasShips')
            if self.shipYard.level > 0: keys.append('hasShipYard')
            if not self.upgraded: keys.append('canBuild')
            if self.usage > 0: keys.append("canHarvest")

            self.info(col, row)
            planetMenu = Menu("What would you like to do on this planet?", inputType='let')
            
            planetMenu.addOptionalItems([
                "Move a ship",
                "Load a ship",
                "Build a ship",
                "Build or upgrade a structure",
                "Harvest resources"
            ],
            [shipMove, shipLoading, buildShip, buildStructure, doHarvest],
            ['hasShips','hasShips',"hasShipYard",'canBuild','canHarvest']
            )
            planetMenu.addItem("See planetary info", doInfo)
            if not planetMenu.menu([keys], galaxy, col, row): break
        # while True:
        #     inp = input(f"What would you like to do at this planet?\nA) Use ships\nB) Build a structure\nC) Harvest Resources\nI) Show info\nX) Leave planet: ").lower()
        #     if inp == 'a':
        #         print()
        #         shipInp = input("Would you like to\nA) Move a ship\nB) Load/Unload a ship\n X) Close").lower()
        #         while True:
        #             if shipInp == 'a':
        #                 super().shipMovementMenu(galaxy, col, row)  
        #             elif shipInp == 'b' :
        #                 self.loadingMenu()
        #             elif shipInp == 'x': break
        #             else: print("Not a valid input")
        #     elif inp == 'b':
        #         print()
        #         self.buildMenu()
        #     elif inp == 'c':
        #         if not self.usage < 1: 
        #             self.harvest()
        #         else: 
        #             print(f"This planet has already been used as much as it can be this turn")
        #     elif inp == 'i':
        #         print()
        #         self.info(col, row)
        #     elif inp == 'x': 
        #         break
        #     else: print("Not a valid input")
        

    def buildMenu(self):
        def upgradeCity(arg):
            if costs.payCost(self.cargo,costs.cityUpgrade(self.civLevel)):
                self.civLevel += 1
                self.upgraded = True
            else: print("You don't have the required resources")
        def buildCity(arg):
            if costs.payCost(self.cargo, costs.city()):
                self.civLevel += 1
                self.upgraded = True
            else: print("You don't have the required resources")
        def buildShipYard(arg):
            if costs.payCost(self.cargo, costs.shipYard()):
                self.shipYard.level += 1
                self.upgraded = True
            else: print("You don't have the required resources")
        def upgradeShipYard(arg):
            if costs.payCost(costs.shipYardUpgrade(self.cargo, self.shipYard.level)):
                self.shipYard.level += 1
                self.upgraded = True
            else: print("You don't have the required resources")
        
        builtCity = self.civLevel > 0
        builtShipYard = self.shipYard.level > 0

        buildMenu = Menu("What would you like to build?", inputType='let', breakAfterEx=True)    
        buildMenu.addOptionalItems([f"Start a city {costs.city()}", f'Upgrade your city {costs.cityUpgrade(self.civLevel)}'], [buildCity, upgradeCity], [False, True])
        buildMenu.addOptionalItems([f"Build a ship yard {costs.shipYard()}", f"Upgrade your ship yard {costs.shipYardUpgrade(self.shipYard.level)}"], [buildShipYard, upgradeShipYard], [False, True])
        buildMenu.menu([[builtCity], [builtShipYard]])

    def reactivate(self):
        super().reactivate()
        self.shipYard.reactivate()
        self.usage = self.civLevel
        self.upgraded = False

    def info(self, col, row):
        print(f"{chr(col + 65)} {row}) ")
        print(f"Planet {self.name}")
        self.cargo.sort()
        for key, value in self.resources.items():
            print(f"{key} {value}, ", end='')
        print()
        for res in self.cargo:
            print(f"{res} ", end='')
        print("")
        self.printStructures()
        self.printShips()
        print(f"")
    
    def printStructures(self):
        print(f"Structures on this planet:")
        if self.civLevel:
            print(f"City level: {self.civLevel}")
            print(f"Activations left this turn {self.usage}")
        if self.upgraded: 
            print("This planet has had a structure built or upgraded this turn")
        if self.shipYard:
            print(f"Ship yard level: {self.shipYard.level}")
    

    def loadingMenu(self, col, row):
        while True:
            self.info(col, row)
            inp = input("pick a ship you would like to move, or enter 'x' to go back: ").lower()
            if inp == 'x': break
            else:
                try:
                    self.moveCargo(int(inp) - 1)
                except: print(f"No ship at index {inp}")

    def moveCargo(self, shipIndex, goingToPlanet, goingToShip):
        while True:
            self.cargo.sort()
            tarShip = self.ships[shipIndex - 1]
            tarShip.cargo.sort()

            print(f"A) {self.name}: " , end='')
            self.loadingDetails(self.cargo)
            print(f"B) To be tranfered to {self.name}: ", end='')
            self.loadingDetails(goingToPlanet)
            print(f"C) To be transfered to the ship: ", end='')
            self.loadingDetails(goingToShip)
            print(f"D) The {tarShip.shipType} ship: ", end='')
            self.loadingDetails(tarShip.cargo)

            inp = input(f"\nWhat resource would you like to move \n(c to finalize, x to cancel, h for help)").lower()
            # complete the move
            if inp == 'c':
                # checking overpacking the ship
                if len(tarShip.cargo) + len(goingToShip) > tarShip.cargoSize:
                    print(f"A {tarShip.shipType} doesn't have enough cargo space to hold all of that")
                    print(f"Please reduce the amount of resources going to the ship to a total of {tarShip.cargoSize}")
                    self.moveCargo(shipIndex, goingToPlanet, goingToShip)
                else:
                    self.cargo.extend(goingToPlanet)
                    tarShip.cargo.extend(goingToShip)
                    tarShip.deactivate()
                    break
            # Cancel the move, return ships to their old values
            elif inp == 'x':
                self.cargo.extend(goingToShip)
                tarShip.cargo.extend(goingToPlanet)
                break

            # Help
            elif inp == 'h':
                self.loadingHelp()
                self.moveCargo(shipIndex, goingToPlanet, goingToShip)

            # Transfer Resources
            else:
                try:
                    takingFrom, resource = inp.split(" ", 1)
                    resource = int(resource)
                    if takingFrom == 'a':
                        goingToShip.append(self.cargo.pop(resource))
                    elif takingFrom == 'b':
                        tarShip.cargo.append(goingToPlanet.pop(resource))
                    elif takingFrom == 'c':
                        self.cargo.append(goingToShip.pop(resource))
                    elif takingFrom == 'd':
                        goingToPlanet.cargo.append(tarShip.cargo.pop(resource))
                    else:
                        print(f"There was an issue with your input (Likely not the correct letter)")
                        input("hit enter to continue")
                except:
                    print(f"There was an issue with your input")
                    input("hit enter to continue")
                    

    def loadingHelp():
        print(f'''To input what you want to move, enter 2 values at once separated by a space:
First the location you are taking a resource from, denoted by the letter
next to where the cargo is printed (ex. Planet = A)
Then the index of the resource you want to move (If you want the first resource from
the planet, you have A 1, make sure you give the space!). The resources that are being moved are held in the 'to be transfered' location
before the move is finalized
              
hit enter to continue...''')
        input('')

    def loadingDetails(self, cargo):
        for i, res in enumerate(cargo):
            print(f"{i + 1}{res} ", end='')
            if i % 10 == 9:
                print('')
        print('')
        
    def harvest(self):
        for resource in self.cargo:
            if resource == 'C':
                self.usage -= 1
                self.cargo.remove(resource)
                result = []
                for key, value in self.resources.items():
                    result.extend([key] * value)
                self.cargo.extend(result)
                return
        # if it has not found a consumable and returned
        print("No consumables to activate planet")
        
        
    

    def genResources(self, type):
        roll = random.randint(1,10)
        if type == 'C' or type == 'F':
            if roll <= 3:
                return 1
            elif roll >= 4 and roll < 6:
                return 2
            elif roll == 6:
                return 3
            else: return 0
 
        elif type == 'M':
            if roll <= 3:
                return 1
            elif roll == 4:
                return 2
            elif roll == 5:
                return 3
            else: return 0

        elif type == 'K' or type == 'D':
            if roll <= 2:
                return 1
            elif roll == 3:
                return 2
            elif roll == 4:
                return 3
            else: return 0

    # List of original, cool fictional planet names
planet_names = [
    "Quoroxia",
    "Vintor",
    "Pluvaria",
    "Gryphus",
    "Stranora",
    "Zelphion",
    "Vorlithe",
    "Crendora",
    "Bluvora",
    "Tolmara",
    "Elveron",
    "Skarnox",
    "Velthra",
    "Quintora",
    "Lynthis",
    "Ortheon",
    "Xenara",
    "Moltrus",
    "Zenquor",
    "Oblivis",
    "Esper",
    "Falo",
    "Zenith",
    "Eden",
    "Awk"

]

# List of Roman numerals and Greek letters for added variety
roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
greek_letters = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa"]

def genName():
    """
    Returns a randomly selected planet name from the list of original fictional planet names,
    appended with either a Roman numeral or a Greek letter for added variety.

    Returns:
    - str: The name of a random original fictional planet with added variety.
    """
    planet = random.choice(planet_names)
    suffix = random.choice([random.choice(roman_numerals), random.choice(greek_letters)])
    return f"{planet}-{suffix}"

