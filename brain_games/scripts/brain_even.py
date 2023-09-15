from brain_games.base.base import process_game
from brain_games.games.even import generate_even_question

EVEN_GAME_START_TEXT = 'Answer "yes" if the number is even, ' \
                       'otherwise answer "no".'


def play():
    """
    Function to play the even game
    """
    process_game(
        question_generator=generate_even_question,
        start_game_text=EVEN_GAME_START_TEXT
    )


def main():
    play()


if __name__ == '__main__':
    main()
