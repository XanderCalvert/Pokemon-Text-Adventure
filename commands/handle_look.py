from settings.text import type_text

# def handle_look(player_data):
#     location = player_data.get('location', 'Unknown location')
#     type_text(f"You are currently in {location}.")
#     # Add more detailed location description logic here if needed.
#     return True, player_data

def handle_look(player_data, locations, object_name=None, action="look"):
    location = player_data['location'].lower()
    if object_name:
        if action == "look":
            type_text(locations[location].look_at(object_name))
        else:
            type_text(locations[location].interact_with(object_name, action))
    else:
        type_text(locations[location].look_around())
    return True, player_data