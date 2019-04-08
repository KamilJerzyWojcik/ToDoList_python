import os
from Models.Colors import Color, printColor
from Models.TaskModel import TaskModel



def addTask(taskModels):
	os.system("clear")
	printColor(text="Set description of task: ", color=Color.BLUE)
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


def addFakeData(taskModels):
	taskModels.append(TaskModel(description="Wyjazd nad morze", startDate="11-07-2019"))
	taskModels.append(TaskModel(description="Wyjście do pracy", startDate="15-03-2019"))
	taskModels.append(TaskModel(description="Wspaniałe wakacje z Karolinką nad morzem", startDate="15-03-2019"))
