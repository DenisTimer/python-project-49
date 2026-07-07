import math
from brain_games.generation import get_number


def is_prime_number(number):
    if number < 2:
        return 'no'
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return 'no'

    return 'yes'

def question_and_answer_prime():
    number = get_number()
    correct_answer = is_prime_number(number)
    return number, correct_answer