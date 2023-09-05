from brain_games.base.consts import GCD_GAME_START_TEXT
from brain_games.base.base import play
from brain_games.games.gcd import generate_gcd_question


def main():
    play(
        question_generator=generate_gcd_question,
        start_game_text=GCD_GAME_START_TEXT
    )


if __name__ == '__main__':
    main()
