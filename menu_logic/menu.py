from save.save_manager import create_new_game, load_game, delete_game

def main_menu():
    while True:
        print("Welcome to Pokémon Text Adventure")
        print("1. New Game")
        print("2. Load Game")
        print("3. Delete Game")
        print("4. Quit")

        choice = input("Chose and option: ")
        if choice == "1":
            return create_new_game()
        elif choice == "2":
            return load_game()
        elif choice == "3":
            return delete_game()
        elif choice == "4":
            print("Goodbye!")
            return None
        else:
            print("iInvalid choice. Please try again")
            return main_menu()