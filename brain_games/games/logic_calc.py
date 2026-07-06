import brain_games.engine.lose as lose
import brain_games.engine.win as win
from brain_games.engine.check_response import is_right
from brain_games.engine.answer import get_answer
from brain_games.engine.generation import get_number, get_operator
from brain_games.engine.question import question
from brain_games.engine.count_rounds import rounds_count as rounds


def get_correct_answer(a, b, operator) -> int:
    result = 0
    match operator:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
    return result


def start_game(name):
    for _ in range(rounds()):
        a, b = get_number(), get_number()
        operator = get_operator()
        question(f'{a} {operator} {b}')
        answer = get_answer()
        correct_answer = get_correct_answer(a, b, operator)
        
        if is_right(answer, str(correct_answer)):
            print('Correct!')
        else:
            return lose.incorrect_answer(answer, correct_answer, name)
        
    return win.congratulations(name)
