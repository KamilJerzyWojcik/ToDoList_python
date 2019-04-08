import os
from Models.Colors import Color, printColor
import datetime
from Models.TaskModel import TaskModel


command = ""
taskModels = []
taskModels.append(TaskModel(description="Wyjazd nad morze", startDate="11-07-2019"))
taskModels.append(TaskModel(description="Wyjście do pracy", startDate="15-03-2019"))
taskModels.append(TaskModel(description="Wspaniałe wakacje z Karolinką nad morzem", startDate="15-03-2019"))




def showMenu():
	printColor(text="..............", color=Color.RED)
	printColor(text="Exit: exit", color=Color.GREEN)
	printColor(text="Add task: add", color=Color.GREEN)
	printColor(text="Show tasks: show", color=Color.GREEN)
	printColor(text="..............", color=Color.RED)
	printColor("")


def addTask():
	os.system("clear")
	printColor(text="Set description of task: ", color=Color.BLUE)
	description = ""
	while True:
		description = input("description (text): ")
		if len(description) < 40:
			break
		else:
			os.system("clear")
			printColor(text="Description can't have more than 40 letters!", color=Color.RED)
			printColor(text="Set description of task: ", color=Color.BLUE)


	printColor(text="Set start day of task: ", color=Color.BLUE)
	dateStart = input("Start day (dd-mm-yyyy): ")
	taskModels.append(TaskModel(description=description, startDate=dateStart))


def showTasks():
	os.system("clear")
	printColor(text="." * 44, color=Color.RED)
	printColor(text="Description" + " " * 9 + " | Date " + " " * 15 + "|")
	printColor(text="." * 44, color=Color.BLUE)

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
			printColor(f"{taskLine[0]} | {task.StartDate}" + " " * 10 + "|")
			printColor(f"{taskLine[1]}" + " " * space + " | " + " " * 20 + "|")
			if lengthTask != index + 1:
				printColor(text="." * 44, color=Color.BLUE)
		else:
			space = 20 - len(taskLine[0])
			printColor(f"{taskLine[0]}" + " " * space + f" | {task.StartDate}" + " " * 10 + "|")
			if lengthTask != index + 1:
				printColor(text="." * 44, color=Color.BLUE)


	printColor(text="." * 44, color=Color.RED)
	printColor("")
	input("press button to back")


while True:
	os.system("clear")
	showMenu()

	command = input("command: ").lower()

	if command == "exit":
		break

	if command == "add":
		addTask()

	if command == "show":
		showTasks()



os.system("clear")





