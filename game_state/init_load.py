import json
import os
from settings.text import type_text

SAVE_DIR = "saves"

def professor_monologue(player_name):
    type_text("Hello there! Welcome to the world of Pokémon!")
    type_text("My name is Oak. People call me the Pokémon Professor.")
    type_text("This world is inhabited by creatures called Pokémon!")
    type_text("For some people, Pokémon are pets. Others use them for fights.")
    type_text("Myself... I study Pokémon as a profession.")
    type_text(f"First, tell me a bit about yourself. You are {player_name}, right?")
    return player_name

def name_rival():
    type_text("This is my grandson. He's been your rival since you were both babies.")
    rival_name = input("...Erm, what is his name again? ")
    return rival_name

def init_load(player_data, filename):
    if not player_data.get('initialized', False):
        player_name = os.path.splitext(os.path.basename(filename))[0]
        player_data['name'] = professor_monologue(player_name)
        player_data['rival'] = name_rival()
        player_data['initialized'] = True

        with open(filename, 'w') as f:
            json.dump(player_data, f, indent=4)

    return player_data
