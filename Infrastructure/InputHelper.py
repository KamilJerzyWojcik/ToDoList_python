from Models.Colors import Color, printColor


def inputYN(communicate):
	while True:
		printColor(text=communicate, color=Color.RED)
		decision = input("decision (y/n): ").lower()
		if decision == "y" or decision == "n":
			break
	return decision

def inputNumberMinMax(communicate, min, max):
	while True:
		number = input(communicate)
		if number.lower() == "exit":
			break
		number = int(number) if number.isdigit() else max + 1
		if number < max and number >= min:
			break
		else:
			printColor(text="Invalid input!", color=Color.RED)
	return number

