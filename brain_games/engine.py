import prompt 
from brain_games.rules import get_rules_brain
from brain_games.question_and_answer import get_question_and_answer


def is_right(answer: str, correct_answer: str) -> bool:
    return answer.lower() == correct_answer


def incorrect_answer(answer, correct_answer, name):
    print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
    print(f"Let's try again, {name}!")


COUNT_ROUNDS = 3


def start_game(name_game, name_gamer):
    print(get_rules_brain(name_game))

    for _ in range(COUNT_ROUNDS):
        question_text, correct_answer = get_question_and_answer(name_game)
        print(f'Question: {question_text}')
        answer = prompt.string('Your answer: ')
        if is_right(answer, correct_answer):
            print('Correct!')
        else:
            return incorrect_answer(answer, correct_answer, name_gamer)
        
    print(f'Congratulations, {name_gamer}!')