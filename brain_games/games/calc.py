from typing import Tuple

from brain_games.base.base import process_game
from brain_games.base.consts import CALC_GAME_START_TEXT
from brain_games.base.randoms import (get_rand_number_from_range,
                                      get_rand_elem_from_seq)


def generate_calc_question() -> Tuple[str, str]:
    """
    Function to generate calculator question with correct answer
    """
    a = get_rand_number_from_range(x=0, y=100)
    b = get_rand_number_from_range(x=0, y=100)
    operator = get_rand_elem_from_seq(['+', '-', '*'])

    question = f'{a} {operator} {b} = ?'

    answer = str(eval(f'{a}{operator}{b}'))

    return question, answer


def play():
    """
    Function to play the calculation game
    """
    process_game(
        question_generator=generate_calc_question,
        start_game_text=CALC_GAME_START_TEXT,
    )
