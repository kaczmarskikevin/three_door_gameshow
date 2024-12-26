from Contestant import Contestant
from Host import Host
from ScoreKeeper import ScoreKeeper
import logging

class Game:

    __contestant__   = None
    __host__         = None
    __score_keeper__ = None

    def __init__(self):
        logging.info("Started a new game")
        self.__contestant__   = Contestant()
        self.__host__         = Host()
        self.__score_keeper__ = ScoreKeeper()

    def play(self, plays):
        logging.info("Let's Play!")

        for i in range(plays):
            logging.debug("\r\n\r\nNew round:")

            #Host presents the three doors. Two have goat and one has a car
            choices = self.__host__.offer_choice()
            logging.debug(f"choices are {choices}")

            #Contestant chooses a random door
            first_choice = self.__contestant__.choose_door(choices)
            logging.debug(f"first choice is {first_choice}")

            #Host allows the contestant to choose the other door.
            new_choices = self.__host__.offer_change(first_choice)
            logging.debug(f"new choices are {new_choices}")

            #The contestant always changes
            second_choice = self.__contestant__.choose_door(new_choices)
            logging.debug(f"second choice is {second_choice}")

            #The host reveals the result of the contestant's choice
            result = self.__host__.reveal_result(second_choice)
            logging.debug("It's a win!" if result else "It's a loss")

            #Record the result and move on
            self.__score_keeper__.book_keep(result)
        
        #Report the results of all games played
        self.__score_keeper__.report_results()

        logging.info("Game Complete")
