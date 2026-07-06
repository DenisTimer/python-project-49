from brain_games.generation import get_number


def get_progression(start, step, length):
    progression = []
    hidden_index = get_number(0, length - 1)
    correct_answer = 0
    for index in range(length):
        current_element = start + index * step
        if index == hidden_index:
            progression.append('..')
            correct_answer = current_element
        else:
            progression.append(str(current_element))
    return progression, correct_answer


def question_and_answer_progression():
    start = get_number()
    step = get_number(1, 10)
    length = get_number(5, 12)
    question_text, correct_answer = get_progression(start, step, length)
    return ' '.join(question_text), str(correct_answer)