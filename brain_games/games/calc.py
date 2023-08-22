import prompt

from brain_games.cli import welcome_user, failure, congratulations
from brain_games.utils.randoms import (get_rand_number_from_range,
                                       get_rand_elem_from_seq)


def play():
    """
    Function to play calculator game
    """
    name = welcome_user(
        additional_text='What is the result of the expression?'
    )
    for _ in range(3):

        a = get_rand_number_from_range(x=0, y=100)
        b = get_rand_number_from_range(x=0, y=100)
        operator = get_rand_elem_from_seq(['+', '-', '*'])

        result = prompt.integer(f'Question: {a} {operator} {b} = ?')

        real_result = eval(f'{a}{operator}{b}')

        if result != real_result:
            failure(
                name=name,
                additional_text=f'"{result}" is wrong answer ;(. '
                                f'Correct answer was "{real_result}".'
            )
            return

        print('Correct!')

    congratulations(
        name=name
    )
