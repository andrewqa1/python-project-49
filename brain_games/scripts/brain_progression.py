from brain_games.base.base import process_game
from brain_games.games.progression import generate_progression_question

PROGRESSION_GAME_START_TEXT = 'What number is missing in the progression?'


if __name__ == '__main__':
    process_game(
        question_generator=generate_progression_question,
        start_game_text=PROGRESSION_GAME_START_TEXT
    )
