from typing import Callable, Tuple

import prompt
from colorama import Fore

BASE_FAILURE_TEXT = '"%s" is wrong answer ;(. Correct answer was "%s"'


def process_game(
        question_generator: Callable[[], Tuple[str, str]],
        start_game_text: str,
):
    """
    Function to process game
    :param start_game_text: Text to show before game starts
    :param question_generator: Callable object to generate question and answer
    """

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(start_game_text)

    for _ in range(3):
        question, answer = question_generator()

        result = prompt.string(f'Question: {question}\nYour answer: ').lower()

        if result != answer:
            print(f'This answer was incorrect! \nLet\'s try again, {name}!')
            print(BASE_FAILURE_TEXT % (result, answer))
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
