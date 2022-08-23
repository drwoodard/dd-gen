import json, os
from monster import Monster, MonsterEncoder
from generators.monster_generator import MonsterGenerator
from tokenizer import StringTokenizer

os.system('clear')

generator = MonsterGenerator()
monster = generator.create("abomination", "random")

print(json.dumps(monster, cls=MonsterEncoder, indent=2))


