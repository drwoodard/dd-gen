import json
import string # can remove
from types import SimpleNamespace
from monster import Monster, MonsterEncoder
from generators.name_generator import MonsterNameGenerator
from dice import Dice


class MonsterGenerator:
    def __init__(self) -> None:
        """Generate a monster based on a specifick type
        Types:
        -- abomination
        """
        # self.__perform_actions = perform_actions

    def __fetch_modifier(self, monster, modifier):
        return modifier if isinstance(modifier, int) else getattr(monster, modifier)

    def __perform_actions(self, monster, actions):
        for action in actions:
            attribute_score = Dice.roll(action.sides, action.dice)
            attribute_score += self.__fetch_modifier(monster, action.attribute.modifier)
            setattr(monster, action.attribute.name, attribute_score)

    def create(self, createure_type : string, monster_name : string = "Bobo"):
        monster = None
        with open(f'data/{createure_type}.json', 'r') as json_file:
            monster_def = json.loads(json_file.read(), object_hook=lambda d: SimpleNamespace(**d))
        
        shape_di = monster_def.shape.dice
        times = int(shape_di.times)
        sides = int(shape_di.sides)

        shape_index = Dice.roll(sides, times)
        shape_index = 2 #for testing
        name = monster_name if monster_name != 'random' else MonsterNameGenerator.generate()
        monster = Monster(name)

        #not safe to simply use pop. need an optional chainging approach
        shape_data = [x for x in monster_def.shape.shapes if int(x.index)==shape_index].pop()
        self.__perform_actions(monster, shape_data.actions)

        monster.description = shape_data.outcome

        return monster

