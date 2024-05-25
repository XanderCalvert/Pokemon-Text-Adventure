from .handle_exit import handle_exit
from .handle_debug_wipe import handle_debug_wipe
from .handle_look import handle_look

def handle_command(command, player_data):
    command = command.lower()

    command_functions = {
        "exit": handle_exit,
        "debug wipe": handle_debug_wipe,
        "look": handle_look,
    }

    if command in command_functions:
        return command_functions[command](player_data)
    else:
        print("Invalid command. Try again.")
        return True, player_data