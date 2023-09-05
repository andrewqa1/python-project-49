from brain_games.base.consts import CALC_GAME_START_TEXT
from brain_games.base.base import play
from brain_games.games.calc import generate_calc_question


def main():
    play(
        question_generator=generate_calc_question,
        start_game_text=CALC_GAME_START_TEXT,
    )


if __name__ == '__main__':
    main()
