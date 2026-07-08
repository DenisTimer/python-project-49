"""Rules text for each brain game."""

RULES = {
    'brain_even': (
        'Answer "yes" if the number is even, '
        'otherwise answer "no".'
    ),
    'brain_calc': 'What is the result of the expression?',
    'brain_gcd': 'Find the greatest common divisor of given numbers.',
    'brain_progression': 'What number is missing in the progression?',
    'brain_prime': (
        'Answer "yes" if given number is prime. '
        'Otherwise answer "no".'
    ),
}


def get_rules_brain(name_game: str) -> str:
    return RULES[name_game]