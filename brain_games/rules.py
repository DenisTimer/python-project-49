def get_rules_brain(name_game: str) -> str:
    result = ''
    match name_game:
        case 'brain_even':
            result = 'Answer "yes" if the number is even, otherwise answer "no".'
        case 'brain_calc':
            result = 'What is the result of the expression?'
    return result