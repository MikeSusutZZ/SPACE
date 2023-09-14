from location import Location
import random

class Planet(Location):
    
    def __init__(self):
        super().__init__()
        self.resources = {"C": self.genResources('C'), "F": self.genResources('F'),
                            "M": self.genResources('M'), "K": self.genResources('K'),
                            "D": self.genResources('D')}
        self.name = genName()
        self.cargo = []



    def info(self):
        print(f"Planet {self.name}")
        for key, value in self.resources.items():
            print(f"{key} {value}, ", end='')
        print("\n")
        for res in self.cargo:
            print(f"{res}, ")
        self.printShips()

    def unloadShip(self, shipIndex, cargoIndex):
        self.cargo.append(self.ships[shipIndex - 1].unload(cargoIndex))

    def loadShip(self, shipIndex, cargoIndex):
    toBeLoaded = 
        self.ships[shipIndex].cargo.append(self.cargo)

    def genResources(self, type):
        roll = random.randint(1,10)
        if type == 'C' or type == 'F':
            if roll <= 3:
                return 1
            elif roll == 4 or roll == 5 or roll == 6:
                return 2
            elif roll == 7:
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
roman_numerals = ["", '', '', "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
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

