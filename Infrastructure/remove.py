import os
from Models.Colors import Color, printColor
from Infrastructure.show import showTasks
from Infrastructure.InputHelper import inputYN, inputNumberMinMax


def removeTask(taskModels):
	showTasks(taskModels)
	printColor("")
	idTaskToRemove = inputNumberMinMax(communicate="select task id to remove or exit to back: ",
										min=0, max=len(taskModels))
	if idTaskToRemove == "exit":
		return
	decision = inputYN(communicate=f"Are you sure to delete {idTaskToRemove} task?")
	if decision == "y":
		del taskModels[idTaskToRemove]

