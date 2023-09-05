from typing import Tuple

from brain_games.base.randoms import get_rand_number_from_range


def generate_progression_question() -> Tuple[str, str]:
    """
    Function to generate progression question with correct answer
    """

    start = get_rand_number_from_range()
    step = get_rand_number_from_range(1, 10)
    stop = start + step * get_rand_number_from_range(5, 11)

    progression = [str(number) for number in range(start, stop, step)]

    missed_ind = get_rand_number_from_range(1, len(progression) - 1)

    progression[missed_ind], answer = '..', str(progression[missed_ind])

    question = ' '.join(progression)

    return question, answer
