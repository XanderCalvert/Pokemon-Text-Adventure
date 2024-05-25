import os
from settings.text import type_text

def handle_debug_wipe(player_data):
    type_text("Wiping all saves and exiting the game.")
    saves_dir = "saves"
    for filename in os.listdir(saves_dir):
        file_path = os.path.join(saves_dir, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    return False, player_data
