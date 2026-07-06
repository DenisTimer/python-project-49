import brain_games.engine.lose as lose
import brain_games.engine.win as win
from brain_games.engine.check_response import is_right
from brain_games.engine.answer import get_answer
from brain_games.engine.generation import get_number
from brain_games.engine.question import question
from brain_games.engine.count_rounds import rounds_count as rounds


def get_correct_answer(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def start_game(name):
    for _ in range(rounds()):
        number = get_number()
        question(number)
        answer = get_answer()
        correct_answer = get_correct_answer(number)
        
        if is_right(answer, correct_answer):
            print('Correct!')
        else:
            return lose.incorrect_answer(answer, correct_answer, name)
        
    return win.congratulations(name)
