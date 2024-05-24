import unittest
from unittest.mock import patch
from menu_logic.menu import main_menu

class TestMenu(unittest.TestCase):

    # Test cases for the main menu functions.

    @patch("builtins.input", side_effect=["1", "test_user"])
    def test_main_menu_new_game(self, mock_input):
        """
        Test the main menu's New Game option.
        Mocks user input to select 'New Game' and enter the username 'test_user'.
        Asserts that the returned player data contains the correct name.
        """
        player_data = main_menu()
        self.assertEqual(player_data["name"], "test_user")

    @patch("builtins.input", side_effect=["invalid", "4"])
    def test_main_menu_invalid_choice(self, mock_input):
        """
        Test the main menu's handling of an invalid choice.
        Mocks user input to provide an invalid option followed by quitting the game.
        Asserts that no player data is returned.
        """
        player_data = main_menu()
        self.assertIsNone(player_data)

if __name__ == "__main__":
    unittest.main()