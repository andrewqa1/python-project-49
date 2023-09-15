from typing import Tuple

from brain_games.base.base import process_game
from brain_games.base.randoms import get_rand_number_from_range

EVEN_GAME_START_TEXT = 'Answer "yes" if the number is even, ' \
                       'otherwise answer "no".'


def generate_even_question() -> Tuple[str, str]:
    """
    Function to generate even question with correct answer
    """
    number = get_rand_number_from_range()
    answer = 'yes' if number % 2 == 0 else 'no'

    return str(number), answer


def play():
    process_game(
        question_generator=generate_even_question,
        start_game_text=EVEN_GAME_START_TEXT)
