
def main():
    from ship import Ship
    newShip = Ship()
    newShip.cargo.append("F")
    newShip.cargo.append("F")
    newShip.printCargo()

if __name__ == "__main__":
    main()