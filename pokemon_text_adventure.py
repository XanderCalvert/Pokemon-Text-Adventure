from save.save_manager import ensure_save_dir_exists
from menu_logic.menu import main_menu

if __name__ == "__main__":
    ensure_save_dir_exists()
    player_data = main_menu()
    if player_data:
        print("You didn't crash yet!")
        pass

"""
This file is part of the Pokemon-Text-Adventure package.

(c) Matt Calvert - https://github.com/XanderCalvert

This source file is subject to the MIT Licence with Additional Commercial
Restriction that is bundled with this source code in the file LICENSE.
"""
