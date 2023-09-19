from ship import Ship
from location import Location
from planet import Planet
from galaxy import Galaxy
def main():
    
    newShip = Ship()
    newShip.cargo.append("F")
    newShip.cargo.append("F")
    newShip.cargo.append('C')
    newShip.cargo.append("K")
    
    galaxy = Galaxy(3)
    galaxy.locations[0][0] = Planet()
    galaxy.info()
    loc = galaxy.locations[0][0]
    loc.gather()
    loc.shipArrives(newShip)
    loc.info()
    loc.moveCargo(1, [], [])
    loc.info()


if __name__ == "__main__":
    main()