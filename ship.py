class Ship:
    def __init__(self):
        self.cargo = []
        self.used = False

    def reactivate(self):
        self.used = False

    def deactivate(self):
        self.used = True

    # def moved():
    #     for resource in self.cargo:
    #         if resource == 'F'


    def printCargo(self):
        for count, resource in enumerate(self.cargo):
            print(f"{count + 1} {resource}, ", end='')
        print(" ")

    def unload(index, self):
        return self.cargo.pop(index - 1)
    
    def load(self, resource):
        if len(self.cargo) < self.cargoLimit:
            self.cargo.append(resource)
        else: return False
