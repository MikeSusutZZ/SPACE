from ship import Ship
from location import Location
from planet import Planet
from galaxy import Galaxy
import costs

def play():
    planet = Planet()
    planet.usage = 5
    planet.cargo.extend(['C', 'M', 'M'])
    planet.info(1,1)
    print(costs.payCost(planet.cargo, costs.cargoShip()))
    planet.info(1,1)

if __name__ == "__main__":
    play()