from brain_games.scripts.brain_games import main as greeting
from brain_games.engine import rules
from brain_games.games import logic_calc


def main():
    name = greeting()
    rules.rules_brain_calc()
    logic_calc.start_game(name)


if __name__ == '__main__':
    main()
