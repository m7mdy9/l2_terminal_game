# Importing our lovely modules!
import sys
import time
import random

"""
Hey so to make sure I am on no wrong ground, here are the bis of code which I have searched for on how to do it
and got it from the internet and I believe I understand it okayyy so yea!
Where I learnt about *args from: https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments
Where I learn the .lower() function: https://www.programiz.com/python-programming/methods/string/lower
Where I learn about setting default arguments: https://thepythoncodingbook.com/2022/11/23/optional-arguments-with-default-values-in-python-functions/
Where I learn about the cool letter by letter print-style: https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
"""
# This part of block is used to save time while testing.
dev_mode = False
def dev_check():
    # Making the variable global so it can be used outside the function
    global dev_mode
    dev_mode = eval(f"{input("Dev Mode? True/False: ")}")

# Saving time on writing time.sleep.... (unfortunately unlike JS's commonjs i can't just do { sleep } = require("time"))
def sleep(n):
    if dev_mode:
        time.sleep(0)
    else:
        time.sleep(n)

# Random choice!! saving time on random.choice()
def rand_choice(list):
    return random.choice(list)

# An animated print!
def anim_print(text, same_line=False):
    # Making the variable global so it can be used outside the function
    global used_text

    # This block of code is responsible for whether to have a line at the end or not since this follows rules different from print().
    if same_line:
        used_text = text
    else:
        used_text = "\n" + text
    # A for loop to write each character by hand using the standrad output
    for char in used_text:
        # Writes character by hand and then flushes the stream in order to have them actually animate.
        sys.stdout.write(char)
        sys.stdout.flush()
        # Part responsible for waiting otherwise it would be just a bad slow print that doesn't look cool while coming in letter by letter
        # Also checking for dev_mode to save my time!
        if dev_mode:
            time.sleep(0.009)
        else:
            time.sleep(0.03)

# input loop that well, makes a loop for input and if wrong input is put it loops till user puts correct one!
def input_loop(*args):
    looper = True
    sleep_print(f"Make your choice (e.g. {args[0]}):", 0.5)
    while looper:
        # making vaariable global to be used else-where
        result = input("\n>")
        if result not in args:
            anim_print(f"Invalid choice. Choose one of the following {args}")
        else:
            looper = False
    return result

# sleep and print
def sleep_print(text, n, i=False):
    sleep(n)
    anim_print(text, i)

# looping sleep and print!
def loop_sp(n, *args):
    for arg in args:
        sleep(n)
        anim_print(arg)

# introduction
def intro():
    sleep_print("Your head hurts.", 1, True)
    loop_sp(1, 
            "You wake up in what seems to be a jungle...", 
            "Looking above you, you can see a parachute stuck in the branches above.",
            "No wonder your head hurts.",
            )
    sleep_print("You stand to evaluate what to do next...", 1)
    sleep_print("\nYou decide that what you will be doing next is...", 2.5)
    loop_sp(1, 
            "1. Walk in a straight line!", 
            "2. Look around and see if there are anywhere worth going."
            )
    global res1
    res1 = input_loop('1', '2')

# actions to carry out for straight_line choice

def straight_line():
    animal = rand_choice(["Tiger", "Lion", "Bear"])
    loop_sp(1, "You decide to move in a straight line...",
            "Congratulations! As a result of your actions you found a...",
            animal + "!",
            "Fortunately, it didn't hear you yet...",
            "Now, you have a choice to make!",
            "1. Wait behind a bush waiting for it to finish whatever it's doing.",
            "2. Sneak around it."
            )
    result = input_loop("1", "2")
    if result == "1":
        return wait_choice(animal.lower())
    elif result == "2":
        return sneak_choice(animal.lower())
    
# the function for the wait choice
def wait_choice(animal):
    loop_sp(2, "You decide to wait...",
            "And wait.....",
            "This is taking longer than expected...",
            "You peek out and you find...",
            f"Another {animal}!",
            "After around 2 hours of waiting, you are left alone wihtout danger!",
            "You decide it's best to continue forward for a few hours and lucky you found a city",
            "After that you went there and managed to get back to your home town!"
            )
    sleep_print("Patience ending!", 2)
    return 10


# the function for the sneak choice
def sneak_choice(animal):
    loop_sp(2, f"You try to sneak around the {animal}",
            f"However, you failed to sneak past it as you stepped on a small but loud tree branch on the ground, and the {animal} hears you.",
            f"Congratulations! You have became the dinner for that {animal}",
            "Dinner ending!"
            )
    return 0

# actions to carry out for look_around choice
def look_around():
    distance = random.randint(1, 99) / 10 
    loop_sp(1.5, f"You look around and you find a temple that is {distance} km away!",
            "Would you like to go to that temple?", "1. Yes.", "2. Sure.", "3. I am uncertain...", "4. Seems like a bad idea.", "5. No.")
    result = input_loop("1", "2", "3", "4" ,"5")
    if result == "1" or result == "2":
        return proceed()
    elif result == "3":
        loop_sp(1.5, "Fine, I will just choose for you then.")
        # For some reason this only chooses 1, hmm weird...
        choice = rand_choice([1,2])
        if choice == 1:
            sleep_print("Proceed, it is!", 1)
            return proceed()
        else: 
            sleep_print("Going somewhere else, it is!", 1)
            return do_not_proceed()
    elif result == "4" or result == "5":
        return do_not_proceed()

# choosing yes in look around choice.
def proceed():
    loop_sp(1.5, "You decide it's a good idea to enter the temple...",
            "You press on a pressure plate while entering, from the looks of it it seems unavoidable",
            "However, the moment you look infront of you, you get greeted by an arrow.",
            "Needless to say, you didn't survive that...",
            "Temple ending!!"
            )
    return 0

# no proceeding :( (as in the user didn't choose to proceed)
def do_not_proceed():
    loop_sp(1.5, 
            'You decide not to proceed!', 
            "You walk for sometime and you find water, life's treating you huh?",
            "You walk for a bit more and you found a city!",
            "You rest there and get some food and then get in some calls.",
            "These calls were able to bring you back home!",
            "Fast ending!!"
            )
    return 10

# main function responsible for the game running
def main():
    while True:
        score = 0
        intro()
        if res1 == "1":
            score = straight_line()
        else:
            score = look_around()
        sleep_print(f"You finished with a score of {score}", 1)
        sleep_print("\nWould you like to play again? y/n:", 1)
        if input_loop('y', 'n') == 'n':
            exit()
        print("\n")

# For dev checking as it allows me to skip over parts and make stuff quicker
# dev_check()
main()