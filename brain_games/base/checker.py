def is_prime(number: int) -> bool:
    """
    Function to know is given number is prime or not
    :param number: given number
    :return: True if given number is prime, otherwise False
    """
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False
