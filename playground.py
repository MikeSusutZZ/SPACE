from ship import Ship
from location import Location
from planet import Planet
from galaxy import Galaxy

def play():
    planet = Planet()
    planet.usage = 5
    planet.cargo.append('C')
    planet.menu()
    

if __name__ == "__main__":
    play()