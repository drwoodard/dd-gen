import random
import linecache
import string
from unicodedata import name


class MonsterNameGenerator:

    @staticmethod
    def generate() -> string:
        name_index = 0

        with open("./data/names.txt", 'r') as name_file:
            lines = name_file.readlines()
            name_index = random.randint(0, len(lines))
            return lines[name_index].strip()