from cargoHolding import CargoDisplay

class Ship(CargoDisplay):
    def __init__(self, type):
        self.cargo = []
        self.cargoSize = 6
        self.shipType = type
        self.used = False

    def reactivate(self):
        self.used = False

    def deactivate(self):
        self.used = True

    def moved(self):
        for resource in self.cargo:
            if resource == 'F':
                self.deactivate()
                self.cargo.remove(resource)
                return True
        print("No fuel")
        return False

    def info(self):
        used = '*'
        if self.used: used = ''
        print(f"{used}{self.shipType} ", end='')
        print(self.displayCargo(self.cargo))
        print("")


    def printCargo(self):
        for count, resource in enumerate(self.cargo):
            print(f"{count + 1} {resource}, ", end='')
        print(" ")

    def unload(self, index):
        return self.cargo.pop(index - 1)
    
    def load(self, resource):
        if len(self.cargo) < self.cargoLimit:
            self.cargo.append(resource)
        else: return False

    def individualMenu(self, args):
        print(f"We made it to indv menu!")