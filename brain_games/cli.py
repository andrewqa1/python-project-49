import prompt


def welcome_user(additional_text: str = '') -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(additional_text)
    return name


def congratulations(name: str, additional_text: str = ''):
    print(f'Congratulations, {name}! {additional_text}')


def failure(name: str, additional_text: str = ''):
    print(f'This answer was incorrect!'
          f'\nLet\'s try again, {name}! {additional_text}')
