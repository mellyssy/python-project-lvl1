from . import cli
from random import randint

def even(player_name):
    score = 0

    while score < 3:
        question = randint(1, 100)
        output = cli.get_num(question) # will return string 'yes' or 'no'

        if question % 2 == 0:
            is_even = 'yes'
        else:
            is_even = 'no'
        
        if output == is_even:
            print('Correct')
            score += 1
        else:
            print(f"'{output}' is wrong answer ;(. Correct answer was '{is_even}'.")
            print(f"Let's try again, {player_name}!")
            break;
    else:
        print(f'Congratulations, {player_name}!')