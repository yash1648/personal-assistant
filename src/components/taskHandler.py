import pyjokes
from datetime import datetime
def joke():
    """Handling the joke command """
    funny=pyjokes.get_joke()
    print(funny)
    return funny


def currenttime():
    """Displaying the current time."""
    current_time = datetime.now()
    return str(current_time)
