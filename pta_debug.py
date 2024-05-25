import os
import json

from save.save_manager import ensure_save_dir_exists
from menu_logic.menu import main_menu
from game_state.init_load import init_load
from commands import handle_debug_command
from settings.text import type_text

if __name__ == "__main__":
    ensure_save_dir_exists()
    player_data = main_menu()
    if player_data:
        player_name = player_data['name']
        save_file = os.path.join("saves", f"{player_name}.json")
        player_data = init_load(player_data, save_file)
        # Start the main game loop here with player_data
        type_text(f"Welcome, {player_data['name']}! Your rival is {player_data['rival']}.")

        running = True
        while running:
            print(" ")
            command = input("> ")
            running, player_data = handle_debug_command(command, player_data)

"""
This file is part of the Pokemon-Text-Adventure package.

(c) Matt Calvert - https://github.com/XanderCalvert

This source file is subject to the MIT Licence with Additional Commercial
Restriction that is bundled with this source code in the file LICENSE.
"""
