import random
import logging

class Host:

    __available_choices__ = None
    __winning_door__      = None

    def __init__(self):
        logging.info("Host created")

    def offer_choice(self):
        self.__available_choices__ = [["car","goat","goat"],["goat","car","goat"],["goat","goat","car"]][random.randrange(3)]
        return self.__available_choices__

    def offer_change(self,contestant_choice):
        self.__available_choices__.remove(contestant_choice)
        self.__available_choices__.remove("goat")
        return self.__available_choices__

    def reveal_result(self,final_choice):
        return "car" == final_choice