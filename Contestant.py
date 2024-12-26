import random
import logging

class Contestant:
    def __init__(self):
        logging.info("Created new contestant")

    def choose_door(self, choices):
        return choices[random.randrange(len(choices))]