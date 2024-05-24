import os
import json

SAVE_DIR = "saves"

def ensure_save_dir_exists():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

def create_new_game():
    username = input("Enter your name: ")
    player_data = {
        "name": username,
        "location": "Childhood Bedroom",
        "pokemon_team": [],
        "items": [],
    }
    save_file = os.path.join(SAVE_DIR, f"{username}.json")
    with open(save_file, "w") as f:
        json.dump(player_data, f, indent=4)
    print(f"New game created for {username}")
    return player_data

def load_game():
    username = input("Enter your name: ")
    save_file = os.path.join(SAVE_DIR, f"{username}.json")
    if os.path.exists(save_file):
        with open(save_file, "r") as f:
            player_data = json.load(f)
        print(f"Game loaded for {username}")
        return player_data
    else:
        print("No saved game found for this name.")
        return None

def delete_game():
    username = input("Enter your name: ")
    save_file = os.path.join(SAVE_DIR,f"{username}.json")
    if os.path.exists(save_file):
        os.remove(save_file)
        print(f"Saved game for {username} deleted")
    else:
        print(f"No saved game found for this name.")