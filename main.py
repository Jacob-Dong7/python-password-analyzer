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
        print("  • Enter '-1' to quit program")
        print("-" * 70)
        name = input("OPTIONAL - ENTER YOUR NAME (First Name + Last Name or First Name): ")

        if name == "-1":
            exit_msg()
            return
        
        name = name.split()
        if len(name) == 2:
            first = name[0]
            last = name[1]
        elif len(name) == 1:
            first = name[0]
            last = None
        else:
            first = None
            last = None

        password = "".join(input("ENTER PASSWORD: ").split())
        print("=" * 70)

        if not check(password):
            continue
        elif password == "-1":
            exit_msg()
            return
        else:
            analyzer = Core(password, first, last)
            analyzer.length_check()
            analyzer.variety_check()
            analyzer.repeat_check()
            analyzer.common_password()
            analyzer.name_check()
            analyzer.report()
            continue

def check(password):
     if password is None or len(password) < 2 or len(password) > 14:
        print("INVALID PASSWORD")
        print("PASSWORD MUST BE MORE THAN ONE AND LESS THAN 15 CHARACTERS")
        return False
     else:
         return True

def exit_msg():
        print("=" * 70)
        print("EXITING..........")
        print("=" * 70)
        
if __name__ == "__main__":
    main()
