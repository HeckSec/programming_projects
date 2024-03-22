from sys import exit

def no():
    print("You should try watching sometime! Now go kick some rocks!")

def yes():
    print("That is great! Let's continue!")
    best()

def nfl():
    print("Do you watch the NFL and have a favorite team?")
    watch = input('> ')
    if "No" in watch:
        no()
    elif "Yes" in watch:
        yes()
    else:
        print("You should try answering the question with yes or no...")

def best():
    print("Who is currently the best team in the NFL?")
    team = input('> ')

    if "Chiefs" in team:
        print("This is the right answer!")
    else:
        print("The powerrankings are bullshit. Try a real team.")

nfl()
