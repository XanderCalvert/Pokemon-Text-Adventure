from .handle_exit import handle_exit
from .handle_look import handle_look
from .handle_help import handle_help
from .handle_debug_wipe import handle_debug_wipe  # Import the debug command

def handle_command(command, player_data):
    command = command.lower()

    command_functions = {
        "exit": handle_exit,
        "look": handle_look,
        "help": handle_help,
    }

    if command in command_functions:
        return command_functions[command](player_data)
    else:
        print("Invalid command. Try again.")
        return True, player_data

def handle_debug_command(command, player_data):
    command = command.lower()

    command_functions = {
        "exit": handle_exit,
        "look": handle_look,
        "help": handle_help,
        "debug wipe": handle_debug_wipe,  # Add the debug command
    }

    if command in command_functions:
        return command_functions[command](player_data)
    else:
        print("Invalid command. Try again.")
        return True, player_data
