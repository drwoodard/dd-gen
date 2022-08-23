
from numbers import Number
import random

class Dice:
    @staticmethod
    def roll( sides: int, times:int = 1) -> int: 
        """ Roll an n-sided di.
        Arguments:
        sides -- represents the number of sides on the di
        times -- the number of rolls you want to perform. The default is 1
        """
        outcome = 0
  
        for x in range(int(times)):
            outcome += random.randrange(1, sides)

        # This code could use some better testing, I'm re-rolling one di in case of a zero. 
        # This should never happen, but it did
        return outcome if outcome > 0 else Dice.roll(1)