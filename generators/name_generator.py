import random
import string
from abc import ABCMeta, abstractmethod, abstractstaticmethod
from tokenize import Name
from unicodedata import name

class NameGenerator(metaclass=ABCMeta):
    @abstractstaticmethod
    def _generate(filename:string = "names") -> string:
        name_index = 0
        with open(f"./data/{filename}.txt", 'r') as name_file:
            lines = name_file.readlines() #read all the lines into memory
            name_index = random.randint(0, len(lines)) #grab a random line
            return lines[name_index].strip() #return the line, removing any non-printable characters.

class MonsterNameGenerator(NameGenerator):

    @staticmethod
    def generate() -> string:
       return NameGenerator._generate("monster_names")

        

class CharacterNameGenerator(NameGenerator):
    
    @staticmethod
    def generate() -> string:
        return NameGenerator._generate()

