from location import Location
import random
import costs
from menu import Menu
from shipYard import ShipYard
from cargoHolding import CargoDisplay

class Planet(Location, CargoDisplay):
    
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

        def doShipMenu(arg):
            self.shipMenu(arg[0], arg[1], arg[2])
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
            for ship in self.ships:
                if not ship.used: keys.append('hasShips')
                break
            if self.shipYard.usage > 0: keys.append('canBuildShip')
            if not self.upgraded: keys.append('canBuild')
            if self.usage > 0: keys.append("canHarvest")

            self.info(col, row)
            planetMenu = Menu("What would you like to do on this planet?", inputType='let')
            
            planetMenu.addOptionalItems([
                "Use ships",
                "Build a ship",
                "Build or upgrade a structure",
                "Harvest resources"
            ],
            [doShipMenu, buildShip, buildStructure, doHarvest],
            ['hasShips',"canBuildShip",'canBuild','canHarvest']
            )
            planetMenu.addItem("See planetary info", doInfo)
            if not planetMenu.menu([keys], galaxy, col, row): break



    def buildMenu(self):
        def buildCity(arg):
            if costs.payCost(self.cargo, costs.city()):
                self.civLevel += 1
                self.upgraded = True
            else: print("You don't have the required resources")
        def upgradeCity(arg):
            if costs.payCost(self.cargo,costs.cityUpgrade(self.civLevel)):
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
        buildMenu.addOptionalItems([f"Start a city ({self.displayCargo(costs.city())})", f'Upgrade your city ({self.displayCargo(costs.cityUpgrade(self.civLevel))})'], [buildCity, upgradeCity], [False, True])
        buildMenu.addOptionalItems([f"Build a ship yard ({self.displayCargo(costs.shipYard())})", f"Upgrade your ship yard ({self.displayCargo(costs.shipYardUpgrade(self.shipYard.level))})"], [buildShipYard, upgradeShipYard], [False, True])
        buildMenu.menu([[builtCity], [builtShipYard]])

    def reactivate(self):
        super().reactivate()
        self.shipYard.reactivate()
        self.usage = self.civLevel
        self.upgraded = False

    def info(self, col, row):
        print(f"{chr(col + 65)} {row}) ")
        print(f"Planet {self.name}")
        for key, value in self.resources.items():
            print(f"{key} {value}, ", end='')
        print()
        print(f"Cargo: {self.displayCargo(self.cargo)}")
        self.printStructures()
        self.printShips()
    
    def printStructures(self):
        print(f"Structures on this planet:")
        if self.civLevel:
            print(f"City level: {self.civLevel}")
            print(f"Activations left this turn: {self.usage}")
        if self.shipYard.level:
            print(f"Ship yard level: {self.shipYard.level}")
            print(f"Activations left this turn: {self.shipYard.usage}")
        if self.upgraded: 
            print("This planet has had a structure built or upgraded this turn")
    

    def loadingMenu(self, col, row):

        def doMoveCargo(args):
            self.moveCargo(args[0], [], [])
        
        shipOptions = Menu("Available Ships")
        # while True:
        #     self.info(col, row)
        #     inp = input("pick a ship you would like to load/unload, or enter 'x' to go back: ").lower()
        #     if inp == 'x': break
        #     else:
        #         try:
        #             self.moveCargo(int(inp) - 1, [], [])
        #         except IndexError as e: print(f"No ship at index {inp} {e}")

    def moveCargo(self, shipIndex, goingToPlanet, goingToShip):
        tarShip = self.ships[shipIndex - 1]
        if not tarShip.used:
            while True:
                print(f"A) {self.name}: {self.displayCargo(self.cargo)}")
                print(f"B) To be tranfered to {self.name}: {self.displayCargo(goingToPlanet)}")
                print(f"C) To be transfered to the ship: {self.displayCargo(goingToShip)}")
                print(f"D) The {tarShip.shipType} ship:{self.displayCargo(tarShip.cargo)} ")

                inp = input(f"\nWhat resource would you like to move \n(c to finalize, x to cancel, h for help)").lower()
                # complete the move
                if inp == 'c':
                    # checking overpacking the ship
                    if len(tarShip.cargo) + len(goingToShip) > tarShip.cargoSize:
                        print(f"A {tarShip.shipType} doesn't have enough cargo space to hold all of that")
                        print(f"Please reduce the amount of resources going to the ship to a total of {tarShip.cargoSize}")
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

                # Transfer Resources
                else:
                    try:
                        takingFrom, resource = inp.split(" ", 1)
                        if takingFrom == 'a':
                            self.sendResource(resource, self.cargo, goingToShip)
                        elif takingFrom == 'b':
                            self.sendResource(resource, goingToPlanet, tarShip.cargo)
                        elif takingFrom == 'c':
                            self.sendResource(resource, goingToShip, self.cargo)
                        elif takingFrom == 'd':
                            self.sendResource(resource, tarShip.cargo, goingToPlanet)
                        else:
                            print(f"There was an issue with your input (Likely not the correct letter)")
                            input("hit enter to continue")
                    except ValueError as e:
                        print(f"There was an issue with your input {e}")
                        input("hit enter to continue")
        else: print(f"That ship has already been used this turn")
                    
    def sendResource(self, targetRes, takeFrom, sendTo):
        for i, res in enumerate(takeFrom):
            if res == targetRes.upper():
                sendTo.append(takeFrom.pop(i))
                break

    def loadingHelp(self):
        print(f'''To input what you want to move, enter 2 values at once separated by a space:
First the location you are taking a resource from, denoted by the letter
next to where the cargo is printed (ex. Planet = A)
Then the index of the resource you want to move (If you want the first resource from
the planet, you have A 1, make sure you give the space!). The resources that are being moved are held in the 'to be transfered' location
before the move is finalized
              
hit enter to continue...''')
        input('')

        
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

