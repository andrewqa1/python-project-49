import prompt

from brain_games.cli import welcome_user, failure, congratulations
from brain_games.utils.randoms import get_rand_number_from_range


def play():
    """
    Function to play even game
    """
    name = welcome_user(
        additional_text='Answer "yes" if the number is even, '
                        'otherwise answer "no".'
    )

    answer_map = {
        'yes': 0,
        'no': 1
    }

    for _ in range(3):

        number = get_rand_number_from_range()
        answer = prompt.regex(
            pattern='^(?i:yes)|^(?i:no)$',
            prompt=f'Question: {number}\n'
        )

        answers = list(answer_map.keys())

        if answer_map[answer.string.lower()] != number % 2:
            answers.remove(answer.string.lower())
            failure(
                name=name,
                additional_text=f'"{answer.string.lower()}" is wrong answer ;(.'
                                f'Correct answer was "{answers[0]}".'
            )
            return

        print('Correct!')

    congratulations(name=name)
