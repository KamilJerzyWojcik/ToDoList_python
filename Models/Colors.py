from enum import Enum
from termcolor import colored


class Color(Enum):
	GREY = "grey"
	RED = 'red'
	GREEN = "green"
	YELLOW = "yellow"
	BLUE = "blue"
	MAGNETA = "magneta"
	CYAN = "cyan"
	WHITE = "white"


def printColor(text, color=Color.WHITE):
	print(colored(text, color.value))
