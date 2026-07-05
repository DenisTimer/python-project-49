from brain_games import number_even, rules
from brain_games.scripts.brain_games import main as greeting


def main():
    name = greeting()
    rules.rules_number_even()
    number_even.start_game(name)


if __name__ == '__main__':
    main()
