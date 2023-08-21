import prompt


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def welcome_even_game() -> str:
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def congratulations(name: str, additional_text: str = ''):
    print(f'Congratulations, {name}! {additional_text}')


def failure(name: str, additional_text: str = ''):
    print(f'This answer was incorrect!'
          f'\nLet\'s try again, {name}! {additional_text}')
