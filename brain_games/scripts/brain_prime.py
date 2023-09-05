from brain_games.base.consts import PRIME_GAME_START_TEXT
from brain_games.base.base import play
from brain_games.games.prime import generate_prime_question


def main():
    play(
        question_generator=generate_prime_question,
        start_game_text=PRIME_GAME_START_TEXT
    )


if __name__ == '__main__':
    main()
