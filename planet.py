from location import Location
import random

class Planet(Location):
    
    def __init__(self):

        self.resources = {"C": self.genResources('C'), "F": self.genResources('F'), "M": self.genResources('M'), "K": self.genResources('K'), "D": self.genResources('D')}
        
    
    def genResources(type):
        roll = random.randint(1,10)
        if type == 'C' or type == 'F':
            if roll <= 3:
                return 1
            elif roll == 4 or roll == 5 or roll == 6:
                return 2
            elif roll == 7:
                return 3
            else: return 0

        if type == 'M':
            if roll <= 3:
                return 1
            elif roll == 4:
                return 2
            elif roll == 5:
                return 3
            else: return 0

        if type == 'K' or type == 'D':
            if roll <= 2:
                return 1
            elif roll == 3:
                return 2
            elif roll == 4:
                return 3
            else: return 0
