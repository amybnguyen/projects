from gym import Gym


def main():
    gym = Gym()
    print(gym.display_bar())
    while True:
        action = input("What would you like to do? (U to update bar, V to view bar) ")
        if action.upper() == "U":
            while True:
                try:
                    target = int(input("What's your target weight? "))
                    break
                except ValueError:
                    print("Please enter a number.")
                    continue
            print(gym.update_bar(target))
            print()
        elif action.upper() == "V":
            print(gym.display_bar())
            print()
        elif action == "stop":
            break


if __name__ == "__main__":
    main()
