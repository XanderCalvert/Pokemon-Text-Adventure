import unittest
from unittest.mock import patch
import os
import json
from save.save_manager import ensure_save_dir_exists, create_new_game, load_game, delete_game, SAVE_DIR

class TestSaveManager(unittest.TestCase):

    def setUp(self):
        ensure_save_dir_exists()
        self.username = "test_user"
        self.save_file = os.path.join(SAVE_DIR, f"{self.username}.json")

    def tearDown(self):
        if os.path.exists(self.save_file):
            os.remove(self.save_file)
    
    @patch("builtins.input", side_effect=["test_user"])
    def test_create_new_game(self, mock_input):
        player_data = create_new_game()
        self.assertTrue(os.path.exists(self.save_file))
        with open(self.save_file, "r") as f:
            data = json.load(f)
        self.assertEqual(data["name"], "test_user")

    @patch("builtins.input", side_effect=["test_user"])
    def test_load_game(self, mock_input):
        player_data = {
            "name": self.username,
            "location": "Childhood Bedroom",
            "pokemon_team": [],
            "items": []
        }
        with open(self.save_file, "w") as f:
            json.dump(player_data, f)
        
        loaded_data = load_game()
        self.assertEqual(loaded_data["name"], self.username)

    @patch("builtins.input", side_effect=["test_user"])
    def test_deleted_game(self, mock_input):
        player_data = {
            "name": self.username,
            "location": "Childhood Bedroom",
            "pokemon_team": [],
            "items": []
        }
        with open(self.save_file, "w") as f:
            json.dump(player_data, f)
        
        delete_game()
        self.assertFalse(os.path.exists(self.save_file))

if __name__ == "__main__":
    unittest.main()