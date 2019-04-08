import os
from Models.Colors import Color, printColor


def showTasks(taskModels):
	os.system("clear")
	numberAsterix = 49
	printColor(text="." * numberAsterix, color=Color.RED)
	printColor(text="lp| Description" + " " * 9 + " | Date " + " " * 15 + "|")
	printColor(text="." * numberAsterix, color=Color.BLUE)

	lengthTask = len(taskModels)

	for index, task in enumerate(taskModels):

		taskLine = []

		if len(task.Description) > 20:
			taskLine.append(task.Description[0:20])
			taskLine.append(task.Description[20:])
		else:
			taskLine.append(task.Description)

		if len(taskLine) > 1:
			space = len(taskLine[0]) - len(taskLine[1])
			printColor(f"{index} | {taskLine[0]} | {task.StartDate}" + " " * 10 + "|")
			printColor(f"  | {taskLine[1]}" + " " * space + " | " + " " * 20 + "|")
			if lengthTask != index + 1:
				printColor(text="." * 44, color=Color.BLUE)
		else:
			space = 20 - len(taskLine[0])
			printColor(f"{index} | {taskLine[0]}" + " " * space + f" | {task.StartDate}" + " " * 10 + "|")
			if lengthTask != index + 1:
				printColor(text="." * numberAsterix, color=Color.BLUE)


	printColor(text="." * numberAsterix, color=Color.RED)



def showMenu():
	printColor(text="..............", color=Color.RED)
	printColor(text="Exit: exit", color=Color.GREEN)
	printColor(text="Add task: add", color=Color.GREEN)
	printColor(text="Show tasks: show", color=Color.GREEN)
	printColor(text="Remove task: remove", color=Color.GREEN)
	printColor(text="..............", color=Color.RED)
	printColor("")
