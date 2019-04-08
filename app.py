import os
from Infrastructure.add import addTask
from Infrastructure.show import showTasks, showMenu
from Infrastructure.remove import removeTask
from Infrastructure.save import saveTasks
from Infrastructure.load import loadTask
from Models.TaskModel import addFakeData


command = ""
taskModels = []
addFakeData(taskModels)

while True:
	os.system("clear")
	showMenu()

	command = input("command: ").lower()

	if command == "exit":
		break

	if command == "add":
		addTask(taskModels)

	if command == "show":
		showTasks(taskModels)
		print("")
		input("press enter to back")

	if command == "remove":
		removeTask(taskModels)

	if command == "save":
		saveTasks(taskModels)

	if command == "load":
		loadTask(taskModels)

os.system("clear")
