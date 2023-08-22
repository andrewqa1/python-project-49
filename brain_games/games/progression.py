import prompt

from brain_games.cli import welcome_user, failure, congratulations
from brain_games.utils.randoms import get_rand_number_from_range


def play():
    """
    Function to play progression game
    """
    name = welcome_user(
        additional_text='What number is missing in the progression? '
    )
    for _ in range(3):

        start = get_rand_number_from_range()
        step = get_rand_number_from_range(1, 10)
        stop = start + step * get_rand_number_from_range(5, 11)

        progression = [str(number) for number in range(start, stop, step)]

        missed_ind = get_rand_number_from_range(1, len(progression) - 1)

        progression[missed_ind], real_number = '..', progression[missed_ind]

        result = prompt.integer(f'Question: {" ".join(progression)}'
                                f'\nYour answer: ')

        if result != real_number:
            failure(
                name=name,
                additional_text=f'"{result}" is wrong answer ;(. '
                                f'Correct answer was "{real_number}".'
            )
            return

        print('Correct!')

    congratulations(
        name=name
    )
