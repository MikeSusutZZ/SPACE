
def city(): return['M','M','M','C','C']

def cityUpgrade(n):
    return ['K', 'M', 'M', 'C'] * n

def shipYard(): return ['M','M','M','F','F','F']

def shipYardUpgrade(n):
    return ['K', 'K', 'M', 'F'] * n

def cargoShip(): return ['M', 'M']

def payCost(cargo, cost):
        collected = []
        # Check if each resource is in the cargo and collect them
        for res in cost:
            if res in cargo:
                collected.append(res)
                cargo.remove(res)
            else:
                # If a resource is not found, add back any collected resources and return False
                cargo.extend(collected)
                return False
        # If all resources were found and collected, return True
        return True