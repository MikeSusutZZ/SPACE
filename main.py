from ship import Ship
from location import Location
from planet import Planet
from galaxy import Galaxy
def main():
    
    newShip = Ship()
    newShip.cargo.append("F")
    newShip.cargo.append("F")
    newShip.printCargo()

if __name__ == "__main__":
    main()