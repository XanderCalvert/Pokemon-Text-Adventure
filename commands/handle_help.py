from settings.text import type_text

def handle_help(player_data):
    help_text = """
    Available commands:
    - exit: Exit the game.
    - look: Describe your current location or an object. Usage: 'look' or 'look <object>'.
    - help: Show this help message.
    - talk <object>: Talk to an interactable object (e.g., talk mum).
    - use <object>: Use an interactable object (e.g., use sink).
    """
    type_text(help_text)
    return True, player_data