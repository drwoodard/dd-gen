

from argparse import ArgumentError
from json import JSONEncoder
import json
import string
from tokenize import String
from xml.dom.minidom import TypeInfo

class Monster:
    def __init__(self, name):
        self.name = name
        self.__description = ''
        self.__hit_points = 0
        self.__armor_class = 0
        self.strength = 0
        self.__dexterity = 0
        self.__intelligence = 0
        self.__wisdom = 0
        self.__constitution = 0
        self.__heads = 1

    @property
    def description(self) -> string:
       return self.__description

    @description.setter
    def description(self, description:string):
        if description and not description.isspace():
            self.__description = description
        else:
            raise ArgumentError(None, "You must supply a description")

    @property
    def heads(self) -> int:
        return self.__heads

    @heads.setter
    def heads(self, quantity:int):
        self.__heads = quantity

    @property
    def hit_points(self) -> int:
        return self.__hit_points
    
    @hit_points.setter
    def hit_points(self, hit_points: int):
        if hit_points > 0 and hit_points < 60:
            self.__hit_points = hit_points
        else:
            raise AttributeError('Hit point values must be between 1 and 60.')


    @property
    def armor_class(self) -> int:
        return self.__armor_class

    @armor_class.setter
    def armor_class(self, value: int):
        if value > 0:
            self.__armor_class = value
        else:
            raise AttributeError("Armor class must be greater than zero.")


## used to return a JSON representation of the Monster
class MonsterEncoder(JSONEncoder):
    def default(self, monster):
        if(isinstance(monster, Monster)):
            return { 
                "name" : monster.name, 
                "description" : monster.description, 
                "hit_points" : monster.hit_points, 
                "heads" : monster.heads,
                "armor_class" : monster.armor_class,
                "strength" : monster.strength
                } 
        
        return super().default(monster)