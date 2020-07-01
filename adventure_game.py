from sys import exit

first_riddle = ['dogs', 'bats', 'mustard', 'flats']
second_riddle = {
    'Donkeys': 'Bailey',
    'Chiefs': 'Gonzalez',
    'Patriots': 'Law',
    'Seahawks': 'Mawae',
    'Ravens': 'Reed',
    'Texans/Chiefs': 'Robinson'
}

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

    if choice.lower() == 'red door':
        print("Is this the path?")
        clown_room()
    elif choice.lower() == 'blue door':
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










start()
