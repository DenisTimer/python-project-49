from brain_games.games.game_calc import question_and_answer_calc
from brain_games.games.game_even import question_and_answer_even
from brain_games.games.game_gcd import question_and_answer_gcd
from brain_games.games.game_progression import question_and_answer_progression
from brain_games.games.game_prime import question_and_answer_prime


def get_question_and_answer(name_game):
    result = ()
    match name_game:
        case 'brain_even':
            result = question_and_answer_even()
        case 'brain_calc':
            result = question_and_answer_calc()
        case 'brain_gcd':
            result = question_and_answer_gcd()
        case 'brain_progression':
            result = question_and_answer_progression()
        case 'brain_prime':
            result = question_and_answer_prime()
    return result