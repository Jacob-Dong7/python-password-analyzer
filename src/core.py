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
        self.full_name = False
        return
    
    def length_check(self):
        self.strength += math.floor(self.length * 2.5)
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
            self.strength += 10
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
        else:
            self.strength += 15

    def common_password(self):
        with open("data/common_passwords.txt", "r") as file:
            for line in file:
                if self.password.lower() == line.strip().lower():
                    self.strength -= 50
                    self.used_common_password = True
    
                    return
        self.strength += 20
    
    def name_check(self):
        first = False
        last = False
        if self.first_name is not None and len(self.first_name) > 3:
            print(len(self.first_name))
            if self.first_name in self.password:
                self.strength -= 50
                self.has_name = True
                first = True

        if self.last_name is not None and len(self.last_name) > 3:
            if self.last_name in self.password:
                self.strength -= 50
                self.has_name = True
                last = True
        if first and last:
            self.full_name = True      
        elif not first and not last:
            self.strength += 5    
        return
    
    def get_grade(self):
        if self.strength < 10:
            return "Very Weak"
        elif self.strength < 30:
            return "Weak"
        elif self.strength < 50:
            return "Medium"
        elif self.strength < 70:
            return "Strong"
        else:
            return "Very Strong"
    
    def report(self):
        print("REPORT")
        print("=" * 70)
        print(f"STRENGTH: {self.get_grade()}")
        if self.strength <= 0:
            print(f"SCORE: 0 / 100")
        elif self.strength >= 100:
            print(f"SCORE: 100 / 100")
        else:
            print(f"SCORE: {self.strength} / 100")
        print("=" * 70)
        print("ISSUES:")
        if self.length != 14:
            print("Password could be longer")
        if self.used_common_password:
            print("Used common password")
        if self.repeat:
            print("Password contains too many repeated characters.")
        if not self.has_upper:
            print("Password does not have uppercase characters")
        if not self.has_lower:
            print("Password does not have lowercase characters")
        if not self.has_digit:
            print("Password does not have digits")
        if not self.has_special:
            print("Password does not have special characters")
        if self.full_name:
            print("The password contains your full name")
        elif self.has_name:
            print("The password contains your first or last name")

    