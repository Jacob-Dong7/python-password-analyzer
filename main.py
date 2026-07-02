from src.core import Core
def main():
    strength = 0
    password = ""
    while True:
        print("=" * 70)
        print("PASSWORD ANALYZER")
        print("=" * 70)
        print("RULE:")
        print("  • Length between 2 and 14")
        print("  • Enter 'EXIT' to quit program")
        print("-" * 70)
        name = input("ENTER YOUR NAME: ")
        name = name.split()
        first = name[0]
        last = name[1]
        password = "".join(input("ENTER PASSWORD: ").split())
        print(f"ENTERED PASSWORD: {password}")
        print("=" * 70)

        if not check(password):
            continue
        elif password == "EXIT":
            print("=" * 70)
            print("EXITING..........")
            print("=" * 70)
            return
        else:
            analyzer = Core(password, first, last)
            #analyzer.length_check()
            #analyzer.variety_check()
            #analyzer.repeat_check()
            analyzer.common_password()
            print(f"Score: {analyzer.get_strength()}")
            continue

def check(password):
     if password is None or len(password) < 2 or len(password) > 14:
        print("INVALID PASSWORD")
        print("PASSWORD MUST BE MORE THAN ONE AND LESS THAN 14 CHARACTERS")
        return False
     else:
         return True

        
if __name__ == "__main__":
    main()
