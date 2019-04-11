import os
from Models.Colors import Color, printColor
from datetime import datetime


def showTasks(taskModels):
	os.system("clear")
	numberAsterix = 75
	printColor(text="." * numberAsterix, color=Color.RED)
	text = "lp| "
	text += "Description" + " " * 9 + " | "
	text += "Date " + " " * 10 + "|"
	text += f" important |"
	text += f"  allDay |"
	text += f" EndDate |"


	printColor(text=text)
	printColor(text="." * numberAsterix, color=Color.BLUE)

	lengthTask = len(taskModels)

	for index, task in enumerate(taskModels):
		task_description_line = []

		if len(task.Description) > 20:
			task_description_line.append(task.Description[0:20])
			task_description_line.append(task.Description[20:])
		else:
			task_description_line.append(task.Description)

		if len(task_description_line) > 1:
			space = len(task_description_line[0]) - len(task_description_line[1])

			line = f"{index} |"
			line += f" {task_description_line[0]} |"
			line += f" {task.StartDate}" + " " * 5 + "|"
			line += " " * 3 + f"{task.Important}" + " " * 3 + "|"
			line += " " * 2 + f"{task.AllDay}" + " " * 2 + "|"
			line += " " * 3 + f"{task.EndDate}" + " " * 2 + "|"

			printColor(line)

			line = f"  | {task_description_line[1]}"
			line += " " * space + " | "
			line += " " * 15 + "|"
			line += " " * 11 + "|"
			line += " " * 9 + "|"
			line += " " * 9 + "|"

			printColor(line)

			if lengthTask != index + 1:
				printColor(text="." * numberAsterix, color=Color.BLUE)
		else:
			space = 20 - len(task_description_line[0])

			line = f"{index} |"
			line += f" {task_description_line[0]}"
			line += " " * space
			line += f" | {task.StartDate}"
			line += " " * 5 + "|"
			line += " " * 3 + f"{task.Important}" + " " * 3 + "|"
			line += " " * 2 + f"{task.AllDay}" + " " * 2 + "|"
			line += " " * 3 + f"{task.EndDate}" + " " * 2 + "|"

			printColor(line)
			if lengthTask != index + 1:
				printColor(text="." * numberAsterix, color=Color.BLUE)


	printColor(text="." * numberAsterix, color=Color.RED)



def showMenu():
	printColor(text="..............", color=Color.RED)
	printColor(text=".....MENU.....", color=Color.RED)
	printColor(text="Exit: exit", color=Color.GREEN)
	printColor(text="Add task: add", color=Color.GREEN)
	printColor(text="Show tasks: show", color=Color.GREEN)
	printColor(text="Remove task: remove", color=Color.GREEN)
	printColor(text="Save tasks: save", color=Color.GREEN)
	printColor(text="Load tasks: load", color=Color.GREEN)
	printColor(text="..............", color=Color.RED)
	printColor("")


def showCurrentTask(taskModels):
	date = datetime.now()
	currentTask = list(filter(lambda x: x.StartDate > date, taskModels))
	currentTask = sorted(currentTask, key=lambda x: x.StartDate)
	color = Color.CYAN
	printColor(f"next task: ", color=Color.RED)
	printColor(f"day:          {currentTask[0].StartDate}", color=color)
	printColor(f"descritprion: {currentTask[0].Description}", color=color)
	printColor(f"important:    {currentTask[0].Important}", color=color)

