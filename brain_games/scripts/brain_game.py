import prompt
from colorama import Fore


def main():
    # print('Welcome to the Brain Games!')
    # name = prompt.string('May I have your name? ')
    # print(f'Hello, {name}!')
    print(Fore.GREEN + 'Welcome to the Brain Games!' + Fore.RESET)
    name = prompt.string(Fore.YELLOW + 'May I have your name? ' + Fore.RESET)
    print(Fore.GREEN + f'Hello, {name}!' + Fore.RESET)
    return name


if __name__ == '__main__':
    main()
