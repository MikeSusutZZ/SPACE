class Ship:
    def __init__(self):
        self.cargo = []
        self.used = False

    def reactivate(self):
        self.used = False

    def deactivate(self):
        self.used = True

    def moved(self):
        for resource in self.cargo:
            if resource == 'F':
                self.deactivate()
                return True
        print("No fuel")
        return False

    def info(self):
        self.printRapid()

    def printCargo(self):
        for count, resource in enumerate(self.cargo):
            print(f"{count + 1} {resource}, ", end='')
        print(" ")

    def printRapid(self):
        for resource in self.cargo:
            print(resource, end="")
        print("")

    def unload(self, index):
        return self.cargo.pop(index - 1)
    
    def load(self, resource):
        if len(self.cargo) < self.cargoLimit:
            self.cargo.append(resource)
        else: return False
