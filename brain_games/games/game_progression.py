from brain_games.generation import get_number


def get_progression(start, step, length):
    progression = []
    correct_answer = 0
    index_answer = get_number(0, length - 1)
    for index in range(length):
        element = start + index * step
        if index == index_answer:
            progression.append('..')
            correct_answer = element
        else:
            progression.append(str(element))
    return progression, correct_answer


def question_and_answer_progression():
    start = get_number()
    step = get_number(1, 10)
    length = get_number(5, 12)
    question_text, correct_answer = get_progression(start, step, length)
    return ' '.join(question_text), str(correct_answer)