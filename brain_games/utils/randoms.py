import random


def get_rand_number_from_range(x: int = -100, y: int = 100) -> int:
    """
    Function to get a random number from given range
    :param x: left side of the range
    :param y: right side of the range
    :return: random number from a given range
    """
    return random.randint(x, y)


def get_rand_elem_from_seq(sequence: list | tuple | str) -> int | float | str:
    """
    Function to get a random element from given sequence
    :param sequence: sequence with elements
    :return: random element from given sequence
    """
    return random.choice(sequence)
