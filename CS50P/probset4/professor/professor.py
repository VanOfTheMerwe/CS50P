import random

# main function containing all of the self-created functions.
def main():
    lvl = get_level()
    generate_integer(lvl)

# get the level the user wants to play at.
def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in [1,2,3]:
                return lvl
        except ValueError:
            pass

# get the game ready.
def generate_integer(level):
    counter = 3
    # counter that allows three mistakes.
    score = 0
    # playerscore that increases with each round.
    for _ in range(10):
        # level selection.
        if level == 1:
            a = random.randint(0,9)
            b = random.randint(0,9)
        elif level == 2:
            a = random.randint(10,99)
            b = random.randint(10,99)
        elif level == 3:
            a = random.randint(100,999)
            b = random.randint(100,999)
        while True:
            try:
                # check if the answers are correct.
                answer = input(f"{a} + {b} = ")
                if int(answer) == (a+b):
                    score += 1
                    # add score if the answers are correct
                    break
                elif answer != (a+b):
                    counter -= 1
                    # if incorrect minus from the mistakes counter
                    print("EEE")
                if counter <= 0:
                    print(f"{a} + {b} = {a+b}")
                    break
            except ValueError:
                pass
    else:
        print(f"Score: {score}")


# call on main to "play the game"
if __name__ == "__main__":
    main()
