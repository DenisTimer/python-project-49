import random


def get_number(start = 1, end = 100):
    number = random.randint(start, end)
    return number


def get_operator():
    operators = [
        '+',
        '-',
        '*'
    ]

    number = random.randint(0, 2)
    return operators[number]
