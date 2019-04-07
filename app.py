import os
from Models.Colors import Color, printColor
from Models.TaskModel import TaskModel
command = ""
taskModels = []


while True:
	os.system("clear")

	printColor(text="..............", color=Color.RED)
	printColor(text="Exit: exit", color=Color.GREEN)
	printColor(text="..............", color=Color.RED)
	printColor("")

	command = input("command: ").lower()
	if command == "exit":
		break

os.system("clear")




