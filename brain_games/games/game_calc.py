from brain_games.generation import get_number, get_operator


def get_correct_answer(a, b, operator) -> str:
    result = 0
    match operator:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
    return str(result)


def question_and_answer_calc():
    a, b = get_number(), get_number()
    operator = get_operator()
    question_text = f'{a} {operator} {b}'
    correct_answer = get_correct_answer(a, b, operator)
    result = (
        question_text,
        correct_answer,
    )
    return result