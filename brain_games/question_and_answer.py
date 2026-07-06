from brain_games.games.game_calc import question_and_answer_calc
from brain_games.games.game_even import question_and_answer_even


def get_question_and_answer(name_game):
    result = ()
    match name_game:
        case 'brain_even':
            result = question_and_answer_even()
        case 'brain_calc':
            result = question_and_answer_calc()
    return result