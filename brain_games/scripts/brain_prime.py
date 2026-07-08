from brain_games.engine import start_game
from brain_games.scripts.brain_games import greet


def main():
    name = greet()
    start_game('brain_prime', name)


if __name__ == '__main__':
    main()
