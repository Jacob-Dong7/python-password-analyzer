import math
class Core:
    def __init__(self, password, first, last):
        self.password = password
        self.length = len(password)
        self.first_name = first
        self.last_name = last
        self.strength = 0
        return
    
    def length_check(self):
        #self.strength += math.floor(self.length * 2.5)
        return self.strength
    
    def variety_check(self):
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        if any(char.isupper() for char in self.password): has_upper = True
        if any(char.islower() for char in self.password): has_lower = True
        if any(not char.isalnum() for char in self.password): has_special = True
        if any(char.isdigit() for char in self.password): has_digit = True

        if has_upper:
            self.strength += 5
        if has_lower:
            self.strength += 5
        if has_special:
            self.strength += 5
        if has_digit:
            self.strength += 5

        return
    
    def repeat_check(self):
        previous = self.password[0]
        repeat_count = 0
        for i in range(1, self.length):
            if self.password[i] == previous:
                repeat_count += 1
            else:
                repeat_count = 0
        if repeat_count >= 3:
            self.strength -= 15


    def get_strength(self) -> int:
        return self.strength
    
    def get_grade(self):
        return
    
    

