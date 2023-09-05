from typing import Tuple

from brain_games.base.randoms import get_rand_number_from_range


def generate_even_question() -> Tuple[str, str]:
    """
    Function to generate even question with correct answer
    """
    number = get_rand_number_from_range()
    answer = 'yes' if number % 2 == 0 else 'no'

    return str(number), answer
