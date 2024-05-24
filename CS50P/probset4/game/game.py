import random
# random library is used because a random number will need to be generated for the game.
def main():
    while True:
        try:
            # get the difficulty level from user.
            level = int(input("Level:"))
            if level > 0:
                break
        except:
            pass
    # generate random number for user to "play" with.
    goal = random.randint(1,level)

    while True:
        try:
            # get the guess from the user.
            guess = int(input('Guess: '))
            # check guess and compare with random number to see if the user wins
            if guess != 0:
                if guess > goal:
                    print('Too large!')
                elif guess < goal:
                    print('Too small!')
                else:
                    # when the user wins the program quits.
                    print('Just Right!')
                    break
        except:
            pass
# calling main to use "best practice" methods.
if __name__ == "__main__":
    main()

