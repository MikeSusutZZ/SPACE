from ship import Ship
from location import Location
from planet import Planet
from galaxy import Galaxy
def main():
    
    newShip = Ship()
    newShip.cargo.append("F")
    newShip.cargo.append("F")
    
    galaxy = Galaxy(3)
    galaxy.locations[0][0] = Planet()
    loc = galaxy.locations[0][0]
    loc.shipArrives(newShip)
    loc.info()
    loc.unloadShip(1,1)
    loc.info()

if __name__ == "__main__":
    main()