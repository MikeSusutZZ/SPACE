from ship import Ship
from location import Location
from planet import Planet
from galaxy import Galaxy
import random
    




def menu(galaxy):
    while checkWin(galaxy):
        galaxy.info()
        try:
            inp = input("Enter the coordinates of where you would like to view (ex: A 1)\nor 'e' to end the round,\n'i' for full galactic info: ")
            if inp.lower() == 'e':
                galaxy.reactivate()
            elif inp.lower() == 'i':
                galaxy.fullInfo()
            else:
                col, row = inp.split(' ', 1)
                print("")
                galaxy.locations[int(row) - 1][ord(col.lower()) - 97].menu(galaxy, ord(col.lower()) - 97, int(row))
        except Exception as e: print(f'Invalid input {e}')


def checkWin(galaxy):
    winStatus = True
    for loc in galaxy.locations:
        if isinstance(loc, Planet) and (loc.settle == True or loc.city == True):
            winStatus = False
    return winStatus

def main():
    print("\n        S.P.A.C.E.\n        Suppy, Prosper, And Conquor Everything! version 0.1\n")
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
    