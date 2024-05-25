from settings.text import type_text

def handle_help(player_data):
    help_text = """
    Available commands:
    - exit: Exit the game.
    - debug wipe: Delete all save files and exit the game.
    - look: Describe your current location.
    - help: Show this help message.
    """
    type_text(help_text)
    return True, player_data
