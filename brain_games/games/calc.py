from typing import Tuple

from brain_games.base.base import process_game
from brain_games.base.randoms import (get_rand_number_from_range,
                                      get_rand_elem_from_seq)

CALC_GAME_START_TEXT = 'What is the result of the expression?'


def generate_calc_question() -> Tuple[str, str]:
    """
    Function to generate calculator question with correct answer
    """
    a = get_rand_number_from_range(x=0, y=100)
    b = get_rand_number_from_range(x=0, y=100)
    operator = get_rand_elem_from_seq(['+', '-', '*'])

    question = f'{a} {operator} {b} = ?'

    calculation_map = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
    }

    answer = str(calculation_map[operator](a, b))

    return question, answer


def play():
    process_game(
        question_generator=generate_calc_question,
        start_game_text=CALC_GAME_START_TEXT,
    )
