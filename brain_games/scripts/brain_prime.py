from brain_games.base.base import process_game
from brain_games.games.prime import generate_prime_question

PRIME_GAME_START_TEXT = 'Answer "yes" if given number is prime. ' \
                        'Otherwise answer "no".'


def play():
    """
    Function to play the prime game
    """
    process_game(
        question_generator=generate_prime_question,
        start_game_text=PRIME_GAME_START_TEXT
    )


def main():
    play()


if __name__ == '__main__':
    main()
