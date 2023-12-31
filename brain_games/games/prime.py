from typing import Tuple

from brain_games.base.base import process_game
from brain_games.base.randoms import get_rand_number_from_range

PRIME_GAME_START_TEXT = 'Answer "yes" if given number is prime. ' \
                        'Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """
    Function to know is given number is prime or not
    :param number: given number
    :return: True if given number is prime, otherwise False
    """
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False


def generate_prime_question() -> Tuple[str, str]:
    """
    Function to generate prime question with correct answer
    """

    question = get_rand_number_from_range(x=0, y=1000)
    answer = 'yes' if is_prime(question) else 'no'

    return str(question), answer


def play():
    process_game(
        question_generator=generate_prime_question,
        start_game_text=PRIME_GAME_START_TEXT
    )
