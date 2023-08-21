from math import gcd

import prompt

from brain_games.cli import welcome_user, failure, congratulations
from brain_games.utils.randoms import get_rand_number_from_range


def play():
    name = welcome_user(
        additional_text='Find the greatest common divisor of given numbers. '
    )
    for _ in range(3):

        a = get_rand_number_from_range(x=0, y=100)
        b = get_rand_number_from_range(x=0, y=100)

        result = prompt.integer(f'Question: {a} {b}')

        real_result = gcd(a, b)

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
