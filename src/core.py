import math
class Core:
    def __init__(self, password, first, last):
        self.password = password
        self.length = len(password)
        self.first_name = first
        self.last_name = last
        self.strength = 0

        self.used_common_password = False
        self.repeat = False
        self.has_upper = False
        self.has_lower = False
        self.has_digit = False
        self.has_special = False
        self.has_name = False
        return
    
    def length_check(self):
        #self.strength += math.floor(self.length * 2.5)
        return self.strength
    
    def variety_check(self):
        if any(char.isupper() for char in self.password): self.has_upper = True
        if any(char.islower() for char in self.password): self.has_lower = True
        if any(not char.isalnum() for char in self.password): self.has_special = True
        if any(char.isdigit() for char in self.password): self.has_digit = True

        if self.has_upper:
            self.strength += 5
        if self.has_lower:
            self.strength += 5
        if self.has_special:
            self.strength += 5
        if self.has_digit:
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
            self.repeat = True
            self.strength -= 15

    def common_password(self):
        with open("data/common_passwords.txt", "r") as file:
            for line in file:
                print(self.password)
                if self.password.lower() == line.strip().lower():
                    self.strength -= 50
    
                    return
    
    def name_check(self):
        if self.first_name in self.password or self.last_name in self.password:
            self.strength -= 50
            self.has_name = True
            print("f")

                
        return
    def get_strength(self) -> int:
        return self.strength
    
    def get_grade(self):
        return
    
    

