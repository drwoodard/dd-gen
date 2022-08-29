import json, os
from generators.name_generator import CharacterNameGenerator
from monster import Monster, MonsterEncoder
from generators.monster_generator import MonsterGenerator
from tokenizer import StringTokenizer

os.system('clear')

generator = MonsterGenerator()
monster = generator.create("abomination", "random")

monsters = []

for x in range(3):
    monsters.append(generator.create("abomination", "random"))


print(json.dumps(monsters, cls=MonsterEncoder, indent=2))

print(CharacterNameGenerator.generate())




