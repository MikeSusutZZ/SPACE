from ship import Ship
import costs
from menu import Menu
from cargoHolding import CargoDisplay
class ShipYard(CargoDisplay):
    def __init__(self, planet):
        self.usage = 0
        self.level = 0
        self.planet = planet
    
    def menu(self, planet):

        # def buildCargo(planetArg):
        #     planet = planetArg[0]
        #     if costs.payCost(planet.cargo, costs.cargoShip()):
        #         planet.shipArrives(Ship('Cargo'))
        #     else: 
        #         print('Not enough resources')
        
        


        # menu = Menu(planet)
        # menu.addOptionalItems

        while True:
            if self.usage < 1:
                print(f"This ship yard has been used to it's full capacity this round")
                break
            else:
                inp = input(f"Would you like to build a cargo ship? ({self.displayCargo(costs.cargoShip())}) (y/n): ").lower()
                if inp == 'y':
                    if costs.payCost(planet.cargo, costs.cargoShip()):
                        planet.shipArrives(Ship('Cargo'))
                        self.usage -= 1
                    else: 
                        print('Not enough resources')
                else: break

                    

    def availbleShips(self):
        print("A) Cargo Ship (Cargo 6, Combat level 0) Cost: M M")
        if self.level > 1:
            print("B) Fighter (Cargo 3, Combat level 1)")

    def reactivate(self):
        self.usage = self.level