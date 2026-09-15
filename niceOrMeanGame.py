#
# Python:  3.14.5
#
# Author: Isaac GChaniel
#
# Purpose: This is a nice or mean game development exercise
#          it demostrate what I have learnt in the past modules of python



def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice_mean(nice,mean,name)
    

def describe_game(name):
    """
        Check if this is a new game or not,
        If it is new, get the user's name,
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this users's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nThroughout this game, you will face a series of everyday situations.")
                    print("Each time, you must decide whether to make a nice or mean choice.")
                    print("Choose carefully, because your actions will determine how the game ends!")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nYou see someone struggling to carry several bags \nDo you stop to help or walk past? \nNice or Mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nYou stop and help them. \nThey thank you with a huge smile.")
            nice = (nice + 1)
            stop = False
        elif pick == "m":
            print("\nYou walk straight past. \nThey shake their head as you leave.")
            mean = (mean + 1)
            stop = False
        else: # If the user enters anything other than M or N,the loop asks again before continuing to score().
            print("\nPlease enter N for Nice or M for Mean.")

    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    elif mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name):
     # Substitute the {} wildcards with our variable values
     print("\n(^_^)  YOU WIN!  (^_^)")
     print("\n{}, your kindness has paid off! \nPeople remember the way you treated them, \nand you've made plenty of friends along the way.".format(name))
     # call again function and pass in our variables
     again(nice,mean,name)

def lose(nice,mean,name):
     # Substitute the {} wildcards with our variable values
     print("\n(T_T)  GAME OVER  (T_T)")
     print("\n{}, your choices have caught up with you! \nPerhaps it's time to rethink how you treat the people you meet.".format(name))
     # call again function and pass in our variables
     again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        elif choice == "n":
            print("\nSorry to see you go! Thanks for playing!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)







if __name__ == "__main__":
    start()
