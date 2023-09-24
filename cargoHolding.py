class CargoDisplay:

    def displayCargo(self, cargoList):
        count = {'C': 0, 'F': 0, 'M': 0, 'K': 0}

        for res in cargoList:
            if res in count:
                count[res] += 1
        
        copy = count.copy()

        for res, amt in count.items():
            if amt < 1: del copy[res]

        result = ", ".join([f"{value}{key}" for key, value in copy.items()])
        return result
