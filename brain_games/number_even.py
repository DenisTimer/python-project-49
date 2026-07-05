import random
import prompt
from brain_games.count_rounds import rounds_count as rounds
import brain_games.win as win
import brain_games.lose as lose


def number_generation():
    number = random.randint(1, 100)
    return number

def question(number: int):
    print(f'Question: {number}')

def is_right(answer: str, number: int):
    right_answer = 'yes' if number % 2 == 0 else 'no'

    if answer.lower() == right_answer:
        return True
    else:
        return right_answer
    
def start_game(name):
    for _ in range(rounds()):
        number = number_generation()
        question(number)
        answer = prompt.string('Your answer: ')
        result = is_right(answer, number)

        if result == True:
            print('Correct!')
        else:
            return lose.incorrect_answer(answer, result, name)
        
    return win.congratulations(name)
