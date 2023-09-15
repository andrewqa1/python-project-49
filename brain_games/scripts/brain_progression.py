from brain_games.base.base import process_game
from brain_games.games.progression import generate_progression_question

PROGRESSION_GAME_START_TEXT = 'What number is missing in the progression?'


def play():
    """
    Function to play the progression game
    """
    process_game(
        question_generator=generate_progression_question,
        start_game_text=PROGRESSION_GAME_START_TEXT
    )


def main():
    play()


if __name__ == '__main__':
    main()
