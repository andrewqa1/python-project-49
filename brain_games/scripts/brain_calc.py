from brain_games.base.base import process_game
from brain_games.games.calc import generate_calc_question

CALC_GAME_START_TEXT = 'What is the result of the expression?'


def play():
    """
    Function to play calculcation game
    """
    process_game(
        question_generator=generate_calc_question,
        start_game_text=CALC_GAME_START_TEXT,
    )


if __name__ == '__main__':
    play()
