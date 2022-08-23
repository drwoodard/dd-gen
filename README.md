# dd-gen

## A starting point for a dd generator.
This is far from complete, but it can serve as a framework for creating the generator.

## Usage
There's a small test harness you can use to generate a partial monster to invoke it call:

> python3 run.py

## Overview
The core of the application is based on "generators". Right now there is one primary generator, the monster_generator.

The core monster is a class that get's created by reading the JSON "abominitation.json" file found in the data folder, however you can pass any monster or character definition file that matches the schema.

There may be other character type generators in the future.

I've also included a sample "random name generator" I took a sample of creature names from here https://5thsrd.org/gamemaster_rules/monster_indexes/monsters_by_name/

Dice logic is fairly established.

I've also built a basic string tokenizer. This allows you to generate the Mad Lib style strings. It currently only supports reading values from your created monster class so there is a dependancy on creating your monster first.

I've more or less solved the dependancies we discussed to allow one stat to be modifed by another. For example you can say that the modifier is derived from the number of heads. The modifiers currently MUST match properties that exist on the object. This will need to be reworked.

Use run.py as a test harness for the application, by running > python3 run.pi
