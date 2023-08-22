import prompt


def welcome_user(additional_text: str = '') -> str:
    """
    Function to welcome user, show additional text
    :param additional_text: text to print after welcome
    :return: name of the user
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(additional_text)
    return name


def congratulations(name: str, additional_text: str = ''):
    """
    Function to congratulate user, show additional text
    :param name: name of the user
    :param additional_text: text to print after congratulation
    """
    print(f'Congratulations, {name}! {additional_text}')


def failure(name: str, additional_text: str = ''):
    """
    Function to failure user, show additional text
    :param name: name of the user
    :param additional_text: text to print after failure
    """
    print(f'This answer was incorrect!'
          f'\nLet\'s try again, {name}! {additional_text}')
