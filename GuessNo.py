import random

randNo = random.randint(1, 100)
userguess = None
guess = 0
print("Press q to quit the game.")

while (True):
    try:
        userguess = input("Guess a number between 1-100: ")
        guess += 1
        if userguess == 'q':
            break
        userguess = int(userguess)
        if userguess == randNo:
            print('\nCorrect Number!')
            print(f"You guessed the number in {guess} tries.\n")
            
        else:
            if userguess > randNo:
                print('\nTry Again! Lower Number Please. ')
            elif userguess< randNo:
                print('\nTry Again! Higher Number Please. ')
    except Exception as e:
        print(f"Your input resulted in an error: {e}")


if userguess != 'q' or userguess == randNo:
    print(f"You guessed the number in {guess} tries.")
else:
    print('Thanks for playing this game.')


with open('highscore.txt', 'r') as f:
    highscore = int(f.read())
if highscore > guess:
    print('\nYou have just broken the highscore! ')
    with open('highscore.txt', 'w') as f:
        f.write(str(guess))
