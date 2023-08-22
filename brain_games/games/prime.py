import prompt

from brain_games.cli import welcome_user, failure, congratulations
from brain_games.utils.checker import is_prime
from brain_games.utils.randoms import get_rand_number_from_range


def play():
    """
    Function to play prime game
    """
    name = welcome_user(
        additional_text='Answer "yes" if given number is prime. '
                        'Otherwise answer "no".'
    )

    answer_map = {
        'yes': True,
        'no': False
    }
    for _ in range(3):

        number = get_rand_number_from_range(x=-1000, y=1000)

        answer = prompt.regex(
            pattern='^(?i:yes)|^(?i:no)$',
            prompt=f'Question: {number}\nYour answer: '
        )

        answers = list(answer_map.keys())

        if answer_map[answer.string.lower()] != is_prime(number):
            answers.remove(answer.string.lower())
            failure(
                name=name,
                additional_text=f'"{answer.string.lower()}" is wrong answer ;(.'
                                f'Correct answer was "{answers[0]}".'
            )
            return

        print('Correct!')

    congratulations(
        name=name
    )
