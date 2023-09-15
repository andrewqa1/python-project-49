from brain_games.base.base import process_game
from brain_games.games.gcd import generate_gcd_question

GCD_GAME_START_TEXT = 'Find the greatest common divisor of ' \
                      'given numbers.'


def play():
    """
    Function to play the gcd game
    """
    process_game(
        question_generator=generate_gcd_question,
        start_game_text=GCD_GAME_START_TEXT
    )


if __name__ == '__main__':
    play()
