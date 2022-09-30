import random

randNo = random.randint(1, 100)
userguess = None
guess = 0
while (userguess != randNo):
    userguess = int(input("Guess a number between 1-100: "))
    guess += 1
    if userguess == randNo:
        print('Correct Number! \n')
    else:
        if userguess > randNo:
            print('\nTry Again! Lower Number Please. ')
        elif userguess< randNo:
           print('\nTry Again! Higher Number Please. ')

print(f"You guessed the number in {guess} tries.")

with open('highscore.txt', 'r') as f:
    highscore = int(f.read())
if highscore > guess:
    print('\nYou have just broken the highscore! ')
    with open('highscore.txt', 'w') as f:
        f.write(str(guess))
