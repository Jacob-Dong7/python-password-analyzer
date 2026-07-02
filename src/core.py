import math
class Core:
    def __init__(self, password):
        self.length = len(password)
        self.strength = 0
        return
    
    def length_check(self):
        self.strength += math.floor(self.length * 2.5)
        return self.strength
    

