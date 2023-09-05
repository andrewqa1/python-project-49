from brain_games.base.consts import PROGRESSION_GAME_START_TEXT
from brain_games.base.base import play
from brain_games.games.progression import generate_progression_question


def main():
    play(
        question_generator=generate_progression_question,
        start_game_text=PROGRESSION_GAME_START_TEXT
    )


if __name__ == '__main__':
    main()
