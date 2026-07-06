import engine.lose as lose
import engine.win as win
import engine.answer as get_anwser
import engine.get_is_right as is_right
from engine.generation import number_generation
from engine.question import question
from engine.count_rounds import rounds_count as rounds


def get_correct_answer(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def start_game(name):
    for _ in range(rounds()):
        number = number_generation()
        question(number)
        answer = get_anwser()
        correct_answer = get_correct_answer(number)
        
        if is_right(answer, correct_answer):
            print('Correct!')
        else:
            return lose.incorrect_answer(answer, correct_answer, name)
        
    return win.congratulations(name)
