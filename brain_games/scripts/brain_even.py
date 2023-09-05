from brain_games.base.consts import EVEN_GAME_START_TEXT
from brain_games.base.base import play
from brain_games.games.even import generate_even_question


def main():
    play(
        question_generator=generate_even_question,
        start_game_text=EVEN_GAME_START_TEXT
    )


if __name__ == '__main__':
    main()
