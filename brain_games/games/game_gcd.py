from brain_games.generation import get_number


def get_correct_answer(a, b) -> str:
    while True:
        if b == 0:
            return str(a)
        a, b = b, a % b


def question_and_answer_gcd():
    a, b = get_number(), get_number()
    question_text = f'{a} {b}'
    correct_answer = get_correct_answer(a, b)
    result = (
        question_text,
        correct_answer,
    )
    return result