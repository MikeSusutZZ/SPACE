from ship import Ship
import costs
class ShipYard():
    def __init__(self, planet):
        self.usage = 1
        self.level = 1
        self.planet = planet
    
    def menu(self, planet):
        while True:
            if self.usage < 1:
                print(f"This ship yard has been used to it's full capacity this round")
            else:
                while self.usage > 0:
                    print("Available Ship at this location are:")
                    self.availbleShips()
                    inp = input("Which ship would you like to build, or 'x' to cancel").lower()
                    if inp == 'a':
                        if costs.payCost(planet.cargo, costs.cargoShip()):
                            planet.shipArrives(Ship('Cargo'))
                    elif inp == 'x':
                        break
                    else:
                        print(f"{inp} is not a valid input")
                    

    def availbleShips(self):
        print("A) Cargo Ship (Cargo 6, Combat level 0) Cost: M M")
        if self.level > 1:
            print("B) Fighter (Cargo 3, Combat level 1)")