import random


def get_number():
    number = random.randint(1, 100)
    return number


def get_operator():
    operators = [
        '+',
        '-',
        '*'
    ]

    number = random.randint(0, 2)
    return operators[number]
