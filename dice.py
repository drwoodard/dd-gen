
from numbers import Number
import random

class Dice:
    """
        A static class to perform basic dice operations.
    """
    # def __init__(self, sides:int) -> None:
    #     self.__sides = sides

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

        return outcome if outcome > 0 else Dice.roll(1)