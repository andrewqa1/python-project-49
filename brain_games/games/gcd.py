from math import gcd
from typing import Tuple

from brain_games.base.randoms import get_rand_number_from_range


def generate_gcd_question() -> Tuple[str, str]:
    """
    Function to generate gcd game question with correct answer
    """

    a = get_rand_number_from_range(x=0, y=100)
    b = get_rand_number_from_range(x=0, y=100)

    question = f'{a} {b}'
    answer = str(gcd(a, b))

    return question, answer
