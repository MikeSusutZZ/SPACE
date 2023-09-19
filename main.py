from ship import Ship
from location import Location
from planet import Planet
from galaxy import Galaxy
import random
    




def menu(galaxy):
    while checkWin(galaxy):
        galaxy.info()
        col, row = (input("Enter the coordinates of where you would like to view (ex: A 1)\n or enter 'e' to end the round: ")).split(' ', 1)
        print("")
        galaxy.locations[ord(col.lower()) - 97][int(row) - 1].menu()


def checkWin(galaxy):
    winStatus = True
    for loc in galaxy.locations:
        if isinstance(loc, Planet) and loc.used == True:
            winStatus = False
    return winStatus

def main():
    print("\n\n     version 0.1\n")
    print("     This game was created by Mike Susut (ZippidyZap, GitHub: MikeSusutZZ)\n")
    print(f"If this is your first time playing, I highly recommend reading the README file\nfirst to learn how the game works!\n")
    seed = input("Do you want to use a seed? (either n or enter seed): ")
    if seed == "n":
        seed = random.randint(0,1000)
        print(f"seed randomly set to {seed}\n")
    random.seed(seed)

    galaxy = Galaxy(5)
    ship = Ship()
    ship.cargo.append("F")
    galaxy.locations[2][2].shipArrives(ship)
    menu(galaxy)

if __name__ == "__main__":
    main()