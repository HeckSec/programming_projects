import random
import sys

def roll(randint):
    return randint
    print(random.randint(0, 6))

print("Would you like to roll the dice?")
dice_roll = input("> ")

if dice_roll == 'Yes':
    print('How bout it! We have ourselves a gambler!')
    # need a function here that simply rolls the dice. Then we call/print results afterwards...
    sum_rolls = roll(random.randint(0, 6)) + roll(random.randint(0, 6))
    print(sum_rolls)
# can we just call one variable here below?
    if sum_rolls == 12:
        print('Boxcars! You stink!')
    elif sum_rolls == 7:
        print('7 is heaven! You win!')
    else:
        print('Bummer, keep going!')
else:
    print('Ok, no problem. Play some other time!')
    exit()
