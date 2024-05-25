from settings.text import type_text

def handle_look(player_data):
    location = player_data.get('location', 'Unknown location')
    type_text(f"You are currently in {location}.")
    # Add more detailed location description logic here if needed.
    return True, player_data
