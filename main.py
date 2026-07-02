from src.core import Core
def main():
    strength = 0
    password = ""
    while password is not "EXIT":
        print("=" * 70)
        print("PASSWORD ANALYZER")
        print("=" * 70)
        print("-" * 70)
        print("RULE:")
        print("  • Length between 2 and 14")
        print("  • Enter 'EXIT' to quit program")
        print("-" * 70)
        password = input("ENTER PASSWORD: ")
        print("=" * 70)

        if password is None or len(password) < 2 or len(password) > 14:
            print("INVALID PASSWORD")
            print("PASSWORD MUST BE MORE THAN ONE AND LESS THAN 14 CHARACTERS")
            continue
        else:
            analyzer = Core(password)
            strength = analyzer.length_check()
            print(strength)
            break
            
    print("-" * 70)
    print("EXITING..........")
    print("-" * 70)
    return


if __name__ == "__main__":
    main()
