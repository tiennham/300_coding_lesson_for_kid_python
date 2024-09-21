import random


def generate_random_integers(n=10, start=0, end=999):
    """
    Generate a list of n random integers between start and end (inclusive).

    :param n: Number of random integers to generate
    :param start: The lower bound of the random integers
    :param end: The upper bound of the random integers
    :return: List of random integers
    """
    random_integers = [random.randint(start, end) for _ in range(n)]
    return random_integers
