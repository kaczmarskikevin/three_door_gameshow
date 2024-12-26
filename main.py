from Game import Game
import logging

LOGGING_LEVEL = logging.INFO

logging.basicConfig(level=LOGGING_LEVEL)

if __name__ == "__main__":
    new_game = Game()
    new_game.play(1000000)