import random


def guess_the_number():

    """Function calls for player input, which should be an integer between 1 an 100 and compares it to random number
       in the same range. Player has to guess the correct number. Function will ask continuously, until the player will
       guess the correct answer, it also gives player some clues, for example: if input is lower than AI_choice,
       function will print "Too small!". Function also check if input is correct."""

    AI_CHOICE = random.randint(1, 100)
    is_guessed = False

    while not is_guessed:
        try:
            player_choice = int(input('Guess the number: '))
            if player_choice not in range(1, 101):
                print('Number not in range of 1-100!')
                continue
        except ValueError:
            print("It's not a number!")
            continue
        if player_choice == AI_CHOICE:
            print('You win!')
            is_guessed = True
        elif player_choice > AI_CHOICE:
            print('Too big!')
        else:
            print('Too small!')


guess_the_number()
