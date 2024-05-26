from .handle_exit import handle_exit
from .handle_look import handle_look
from .handle_help import handle_help
from .handle_debug_wipe import handle_debug_wipe

def handle_command(command, player_data, locations):
    command = command.lower().split()
    if not command:
        print("Invalid command. Try again.")
        return True, player_data

    action = command[0]
    command_functions = {
        "exit": lambda: handle_exit(player_data),
        "look": lambda: handle_look(player_data, locations, command[1] if len(command) > 1 else None),
        "help": lambda: handle_help(player_data),
        "talk": lambda: handle_look(player_data, locations, command[1] if len(command) > 1 else None, "talk"),
        "use": lambda: handle_look(player_data, locations, command[1] if len(command) > 1 else None, "use"),
        "debug wipe": lambda: handle_debug_wipe(player_data)  # Include the debug command for now
    }

    if action in command_functions:
        return command_functions[action]()
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
