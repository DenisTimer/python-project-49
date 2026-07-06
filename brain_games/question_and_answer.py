from brain_games.games.game_calc import question_and_answer_calc
from brain_games.games.game_even import question_and_answer_even
from brain_games.games.game_gcd import question_and_answer_gcd


def get_question_and_answer(name_game):
    result = ()
    match name_game:
        case 'brain_even':
            result = question_and_answer_even()
        case 'brain_calc':
            result = question_and_answer_calc()
        case 'brain_gcd':
            result = question_and_answer_gcd()
    return result