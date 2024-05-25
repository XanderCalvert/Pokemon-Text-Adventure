from settings.text import type_text

def handle_exit(player_data):
    type_text("Exiting the game. Goodbye!")
    return False, player_data