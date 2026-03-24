"""
Program Name: Coin Class
Author: Farouk Bellili
Purpose: This class represents a single coin that can be tossed
         and returns either Heads or Tails.
Starter Code: None
Date: March 24, 2026
"""

import random

class Coin:

    def __init__(self):
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup
