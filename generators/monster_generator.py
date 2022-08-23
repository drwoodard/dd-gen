import json
import string # can remove
from types import SimpleNamespace
from monster import Monster, MonsterEncoder
from generators.name_generator import MonsterNameGenerator
from tokenizer import StringTokenizer
from dice import Dice


class MonsterGenerator:
   
    def create(self, createure_type : string, monster_name : string = "Bobo"):
        monster = None
        with open(f'data/{createure_type}.json', 'r') as json_file:
            monster_def = json.loads(json_file.read(), object_hook=lambda d: SimpleNamespace(**d))
        
        name = monster_name if monster_name != 'random' else MonsterNameGenerator.generate()
        monster = Monster(name)

        shape_data = self.get_data(monster_def.shape.shapes, monster_def.shape.dice)
        self.__perform_actions(monster, shape_data.actions)

        #perform this last since the tokenizer won't be able to resolve un-set properties.
        monster.description =  StringTokenizer.tokenize(shape_data.outcome, monster)

        return monster

    def get_data(self, data, dice):
        index = self.get_index(dice)
        #not safe to simply use pop. need an optional chainging approach
        return [x for x in data if int(x.index)==index].pop()

    def get_index(self, di):
        times = int(di.times)
        sides = int(di.sides)

        #initialize the dice to determine which 
        index = Dice.roll(sides, times)
        index = index if index < 3 else 1 #DELETE THIS LINE. It's used for testing since we don't have all monsters defined
        return index

    def __fetch_modifier(self, monster, modifier):
        return modifier if isinstance(modifier, int) else getattr(monster, modifier)

    def __perform_actions(self, monster, actions):
        for action in actions:
            attribute_score = Dice.roll(action.sides, action.dice)
            attribute_score += self.__fetch_modifier(monster, action.attribute.modifier)
            setattr(monster, action.attribute.name, attribute_score)

