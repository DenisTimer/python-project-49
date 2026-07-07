def get_rules_brain(name_game: str) -> str:
    result = ''
    match name_game:
        case 'brain_even':
            result = 'Answer "yes" if the number is even, otherwise answer "no".'
        case 'brain_calc':
            result = 'What is the result of the expression?'
        case 'brain_gcd':
            result = 'Find the greatest common divisor of given numbers.'
        case 'brain_progression':
            result = 'What number is missing in the progression?'
        case 'brain_prime':
            result = 'Answer "yes" if given number is prime. Otherwise answer "no".'

            
    return result