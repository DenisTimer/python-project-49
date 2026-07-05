from brain_games.scripts.brain_games import main as greeting
from brain_games import rules
from brain_games import number_even

def main():
    name = greeting()
    rules.rules_number_even()
    number_even.start_game(name)

if __name__ == '__main__':
    main()
