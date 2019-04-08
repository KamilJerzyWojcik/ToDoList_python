import os
from Infrastructure.add import *
from Infrastructure.show import *
from Infrastructure.remove import *

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

os.system("clear")
