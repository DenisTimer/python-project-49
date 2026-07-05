import random

import prompt

import brain_games.lose as lose
import brain_games.win as win
from brain_games.count_rounds import rounds_count as rounds


def number_generation():
    number = random.randint(1, 100)
    return number


def question(number: int):
    print(f'Question: {number}')


def get_right(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def is_right(answer: str, correct_answer: str) -> bool:
    return answer.lower() == correct_answer


def start_game(name):
    for _ in range(rounds()):
        number = number_generation()
        question(number)
        answer = prompt.string('Your answer: ')
        correct_answer = get_right(number)
        
        if is_right(answer, correct_answer):
            print('Correct!')
        else:
            return lose.incorrect_answer(answer, correct_answer, name)
        
    return win.congratulations(name)
