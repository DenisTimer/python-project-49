from games import logic_even
from brain_games.scripts.brain_games import main as greeting
from engine import rules


def main():
    name = greeting()
    rules.rules_brain_even()
    logic_even.start_game(name)


if __name__ == '__main__':
    main()
