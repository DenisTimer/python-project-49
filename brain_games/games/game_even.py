from brain_games.generation import get_number


def get_correct_answer(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def question_and_answer_even():
    question_text = get_number()
    correct_answer = get_correct_answer(question_text)
    result = (
        question_text,
        correct_answer,
    )
    return result