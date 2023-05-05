"""Library for handling bot authentication."""

# Imports
import json
import os
import os.path
from typing import Union

# Variables
if os.name == "nt": 
    with open(f"{os.getcwd()}\\config\\startup.json", 'r') as f: config = json.load(f)
else: 
    with open(f"{os.getcwd()}/config/startup.json", 'r') as f: config = json.load(f)

# Functions
def get_token() -> str:
    """Returns the bot token, if provided in the `startup.json` file."""
    return config["auth"]["token"]

def get_public_key() -> str:
    """Returns the bot's public key, if provided in the `startup.json` file."""
    return config["auth"]["public_key"]

def get_owner_id() -> str:
    """Returns the set owner id, if it is provided in the `startup.json` file."""
    return config["extra_metadata"]["owner_id"]

def set_owner_id(id: Union[int, str]) -> bool:
    """
    Sets the owner id. If an existing owner id is in the `startup.json` file, that id will be overwritten with the new one.
    
    Args:
    * id (int/str): The new owner id

    Return:
    * Returns `True` if change successful
    * Returns `False` if change not successful
    """
    try:
        if type(id) == int: id = str(id)
        config["extra_metadata"]["owner_id"] = id
        if os.name == "nt":
            with open(f"{os.getcwd()}\\config\\startup.json", 'w+')  as f: json.dump(config, f, indent=4)
        else:
            with open(f"{os.getcwd()}/config/startup.json", 'w+') as f: json.dump(config, f, indent=4)
        return True
    except Exception as exc:
        print(f"An error occured while trying to save new owner id: {type(exc).__name__}: {exc}")
        return False
