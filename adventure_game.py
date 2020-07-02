from sys import exit

first_riddle = ['dogs', 'bats', 'mustard', 'moon']
second_riddle = {
    'Donkeys': 'Bailey',
    'Chiefs': 'Gonzalez',
    'Patriots': 'Law',
    'Seahawks': 'Mawae',
    'Ravens': 'Reed',
    'Texans/Chiefs': 'Robinson'
}

def first_riddle_fun():
    print("What do the following items have in common?:")
    print(first_riddle[0:])

    string_fun = input("> ")

    if string_fun.lower() == "nothing" or string_fun.lower() == 'nada':
        print("That is correct! Pretty shitty riddle, huh?!")
        print("Try not to open the trap door this time? Back to Hoboken!")
        print("--" * 20)
        hell()

    elif string_fun.lower() == "hint":
        print("Ok, you can have a hint.")
        print("Don't overthink it. Really, it's nothing...")
        print("Now try again!")
        print("--" * 20)
        first_riddle_fun()

    else:
        print("That is not correct, please try again.")
        first_riddle_fun()


def riddle():
    print("This is how you'll earn your way back to the previous room!")
    print("Answer the following question:")
    print("What do the following people have in common?:")
    print("--" * 20)
    # this will print out only the names of the players, not their teams.
    # How can I shorten this? Printing only the second item of a dictionary for all values?
    print(second_riddle['Donkeys'])
    print(second_riddle['Chiefs'])
    print(second_riddle['Patriots'])
    print(second_riddle['Seahawks'])
    print(second_riddle['Ravens'])
    print(second_riddle['Texans/Chiefs'])

    string = input("> ")

    # This is not the full hint.
    if string.lower() == "hint":
        print("--" * 20)
        print("Ok, ok, here is a hint")
        print("These individuals all loved to touch pig skin.")
        print("-----Try Again-----")
        riddle()

    elif string.lower() == "full":
        print("--" * 20)
        print("Ok, ok, you can see the full dictionary! ")
        # This will print out the full dictionary, comprised of both Teams and player names
        print(second_riddle)
        print("-----Try Again-----")
        riddle()

    elif string.lower() == "nfl hall of fame" or string.lower() == "nfl hof" or string.lower() == "2019 nfl hof" or string.lower() == "2019 nfl hall of fame":
        print("Great job! You know your football. Back to the tree room!")
        tree_room()

    else:
        print("Please answer the question, or you'll not be getting anywhere!")
        print("--" * 20)
        riddle()


def start():
    print("You're outside.")
    print("You've stumbled upon an abandoned camper van")
    print("Do you enter?")

    choice = input("> ")

    if choice.lower() == "yes":
        print("Haven't horror movies taught you anything?!")
        tree_room()
    elif choice.lower() == "no":
        print("Well, that's not any fun!")
        exit()
    else:
        print('You got lost and starved, eventually reincarnated as a sloth')
        print("--" * 20)
        start()

def tree_room():
    print("--" * 20)
    print("You're in a room full of trees!")
    print("You see two doors.")
    print("There is a Red door and a Blue door.")
    print("Which do you wish to enter?")

    choice = input("> ")

    if choice.lower() == 'red door' or choice.lower() == 'red':
        print("Is this the path?")
        clown_room()
    elif choice.lower() == 'blue door' or choice.lower() == 'blue':
        print("This will get interesting.")
        wilderness_of_mirrors()
    else:
        print("Please choose either the 'Red door' or 'Blue door'.")
        tree_room()

def wilderness_of_mirrors():
    print("--" * 20)
    print("You're in the wilderness of mirrors!")
    print("You have two options, neither of which look promising.")
    print("Which path do you choose?")
    print("'Outside' or 'Deeper Inside'?")

    choice = input("> ")

    if choice.lower() == "outside":
        print("You're back outside and you must begin again!")
        print("/REBOOT/")
        print("--" * 20)
        start()

    elif choice.lower() == "deeper inside":
        print("You are shot to outer space to hang with stephen hawking!")
        print("Quick, answer this question to get back to the tree room!")
        riddle()

    else:
        print("Please choose either 'Outside' or 'Deeper Inside'")
        wilderness_of_mirrors()

def clown_room():
    print("You have entered the clown room.")
    print("You see a clown staring at you from the corner.")
    print("They have a knife!")
    print("Quick, what do you do?!")
    print("Enter 'Hell' or 'Run Circles'?")

    decision = input("> ")

    if decision.lower() == "hell":
        hell()

    elif decision.lower() == "run circles":
        print("The clown took off their mask!")
        print("But they stabbed you and it doesn't matter who they are because you died.")
        print("/REBOOT/")
        print("--" * 20)
        start()

    else:
        print("--" * 20)
        print("Please choose one of the following:\n-Hell\n-Run Circles")
        clown_room()

def hell():
    print("--" * 20)
    print("Welcome to Hoboken, NJ. You've made a grave mistake!")
    print("You have two choices:\n-enter through Trap Door\n-open the Golden door")
    print("Which will it be?!")

    trap = input("> ")

    if trap.lower() == "trap door" or trap.lower() == "trap":
        print("Why in the world would you choose this option?!")
        print("You'll have to answer a riddle to get back to Hoboken (hell).")
        first_riddle_fun()

    elif trap.lower() == "golden door" or trap.lower() == "gold" or trap.lower() == "golden" or trap.lower() == "gold door":
        print("--" * 20)
        golden_door()

    else:
        print("--" *20)
        print("That is not a valid response.")
        print("Please tell me one of the following options:\n -Trap Door\n -Golden Door")
        hell()


def golden_door():
    print("You've chosen the golden door.")
    print("You're very close to the ultimate prize!")
    print("You've come across a gorgeous lake.\n What do you want to do here?")
    print("--" * 20)
    print("You'll have to tell me. I can't give the answer away!")

    prize = input("> ")

    if prize.lower() == "go fishing":
        print("YOU WON!")
        print("Thank you for playing this adventure game.")
        print("------------(!!!!!!!!!!)------------" * 10)
        print("Fin" * 100)
        exit()

    else:
        print("--" * 20)
        print("--" * 20)
        print("Keep trying!\n You're very close!")
        print("(I actually don't know if you're close, but I figured there is nothing wrong with encouragement.)")
        print("--" * 20)
        print("--" * 20)
        golden_door()









start()
