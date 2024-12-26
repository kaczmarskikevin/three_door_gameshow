import logging

class ScoreKeeper:

    __games__ = None
    __wins__  = None
    __loses__ = None

    def __init__(self):
        logging.info("Score keeper created")
        self.__games__ = 0
        self.__wins__  = 0
        self.__loses__ = 0

    def book_keep(self, result):
        self.__games__ = self.__games__ + 1
        if (result):
            self.__wins__ = self.__wins__ + 1
        else:
            self.__loses__ = self.__loses__ + 1

    def report_results(self):
        logging.info(f"Games: {self.__games__} Wins: {self.__wins__} Loses: {self.__loses__}")
        logging.info(f"Realized Win Rate: {(self.__wins__ / self.__games__ ) * 100}")