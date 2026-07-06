from brain_games.engine import start_game
from brain_games.scripts.brain_games import main as greeting


def main():
    name = greeting()
    start_game('brain_gcd', name)


if __name__ == '__main__':
    main()
