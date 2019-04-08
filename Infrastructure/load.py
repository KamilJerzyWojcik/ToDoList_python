import csv
from Models.TaskModel import TaskModel

def loadTask(taskModels):
	with open(file='Data.csv',  newline='') as taskFile:
		tasks = csv.reader(taskFile, delimiter=',', quotechar='|')
		for task in tasks:
			taskModels.append(TaskModel(description=task[0], startDate=task[1]))
			print(task)

