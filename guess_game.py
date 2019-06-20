# guessing number gambler
import random

print("What is your name?")
name = input("> ")

secret_number = random.randint(0, 20)

# have the user guess 6 Times
for guesses in range (1, 7):
        print(name + ', take a guess at my secret number!')
        guess = int(input("> "))
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            break #this would be the correct guesses
if guess == secret_number:
    print('Good job, ' + name + '! You guessed my number in ' + str(guesses) + ' Guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number))
