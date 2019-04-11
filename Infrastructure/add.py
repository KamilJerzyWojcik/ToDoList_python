import os, re
from Models.Colors import Color, printColor
from Models.TaskModel import TaskModel

dateRegex = "^[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]$"


def addTask(taskModels):
	os.system("clear")
	printColor(text="Set description of task: ", color=Color.BLUE)
	description = descriptionValidation()

	printColor(text="Set start day of task: ", color=Color.BLUE)
	dateStart = dateStartValidation()

	printColor(text="Task is important?: ", color=Color.BLUE)
	important = importantValidation()

	printColor(text="Task is all day?: ", color=Color.BLUE)
	allDay = allDayValidation()


	newTask = TaskModel(description=description, startDate=dateStart)
	newTask.setImportant(important)
	newTask.setAllDay(allDay)

	if allDay == False:
		printColor(text="Set start day of task: ", color=Color.BLUE)
		endDate = endDateValidation()
		newTask.addEndDate(endDate)

	taskModels.append(newTask)



def descriptionValidation():
	while True:
		description = input("description (text): ")
		if 0 < len(description) < 40:
			break
		else:
			os.system("clear")
			printColor(text="Description have to from 1 to 40 letters!", color=Color.RED)
			printColor(text="Set description of task: ", color=Color.BLUE)
	return description


def dateStartValidation():
	while True:
		dateStart = input("Start day (dd-mm-yyyy): ")
		if re.search(dateRegex, dateStart):
			break
		else:
			os.system("clear")
			printColor(text="Date pattern: dd-mm-yyyy", color=Color.RED)
			printColor(text="Start day (dd-mm-yyyy): ", color=Color.BLUE)
	return dateStart


def importantValidation():
	while True:
		important = input("important (y/n): ")
		if important == "y" or important == "n":
			important = True if important == "y" else False
			break
		else:
			os.system("clear")
			printColor(text="Invalid command set y or n", color=Color.RED)
			printColor(text="Task is important?: ", color=Color.BLUE)
	return important


def allDayValidation():
	while True:
		allDay = input("all day (y/n): ")
		if allDay == "y" or allDay == "n":
			allDay = True if allDay == "y" else False
			break
		else:
			os.system("clear")
			printColor(text="Invalid command set y or n", color=Color.RED)
			printColor(text="Task is all day?: ", color=Color.BLUE)
	return allDay


def endDateValidation():
	while True:
		endDate = input("End day (dd-mm-yyyy): ")
		if re.search(dateRegex, endDate):
			break
		else:
			os.system("clear")
			printColor(text="Date pattern: dd-mm-yyyy", color=Color.RED)
			printColor(text="End day (dd-mm-yyyy): ", color=Color.BLUE)
	return endDate
