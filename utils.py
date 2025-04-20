import random

USERNAME_PROMPT = "Enter your username: "


def get_user_to_press_enter():
    user_input = input("Press Enter to continue or type 'exit' to quit: ")


def get_user_input():
    """
    Get user input with a prompt.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        str: The user's input.
    """
    # TODO: add feature to only take string and not numbers
    return input(USERNAME_PROMPT).strip()

def randomize_player_order(players):
    random.shuffle(players)
    return players
