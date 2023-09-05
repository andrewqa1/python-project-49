from typing import Tuple

from brain_games.base.checker import is_prime
from brain_games.base.randoms import get_rand_number_from_range


def generate_prime_question() -> Tuple[str, str]:
    """
    Function to generate prime question with correct answer
    """

    question = get_rand_number_from_range(x=0, y=1000)
    answer = 'yes' if is_prime(question) else 'no'

    return str(question), answer
