# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

"""
References:
1. ipnd-starter-code-master.zip: fill-in-the-blanks.py and fill-in-the-blanks.pyc
2. https://storage.googleapis.com/supplemental_media/udacityu/7710122499/madlibs_generator.py
"""

print "------"
print "Welcome to the IPN Game."
print "------"

waiting_for_user_input = True
game_level = 0
guess_items_in_level = ""
string_to_guess = ""
answers = ""

def play_game(_string_to_guess, _guess_items_in_level, _answers):
    _array_to_guess = _string_to_guess.split()


    for _guess_item in _guess_items_in_level:
        _waiting_for_user_input = True

        while _waiting_for_user_input:
            print ""
            print _string_to_guess
            print ""
            guess = raw_input("Guess an answer for __" + str(_guess_item + 1) + "__: ")
            if guess == _answers[_guess_item]:
                print ""
                print "Correct!"
                print ""
                _waiting_for_user_input = False

                c = 0

                while c < len(_array_to_guess):
                    if _array_to_guess[c] == "___" + str(_guess_item + 1) + "___":
                        print "FOUND: ___" + str(_guess_item  + 1) + "___"
                        _array_to_guess[c] = guess
                    c += 1

    print _array_to_guess


while waiting_for_user_input:

    game_level = raw_input("Select a Level (1, 2, 3): ")

    if game_level == "1":
        print "You picked 1 - Easy."
        string_to_guess = "A ___1___ in ___2___ is created with the def keyword."
        guess_items_in_level = [0, 1]
        answers = ["variable", "Python"]
        waiting_for_user_input = False
    elif game_level == "2":
        waiting_for_user_input = False
    elif game_level == "3":
        waiting_for_user_input = False
    else:
        print "You picked a level that does not exist."

print("You selected level: " + game_level + ".")

play_game(string_to_guess, guess_items_in_level, answers)




#print(user_input)
