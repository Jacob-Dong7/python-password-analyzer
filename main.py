from src.core import Core
def main():
    strength = 0
    while True:
        print("=" * 70)
        print("PASSWORD ANALYZER")
        print("=" * 70)
        password = input("ENTER PASSWORD: ")
        print("=" * 70)

        if password is None or len(password) < 2:
            print("INVALID PASSWORD")
            print("PASSWORD MUST BE MORE THAN ONE CHARACTER")
            continue
        else:
            analyzer = Core(password)
            strength = analyzer.length_check(password)
            print(strength)
            break
            
    return


if __name__ == "__main__":
    main()
