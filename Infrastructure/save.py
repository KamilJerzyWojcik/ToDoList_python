import csv

ENCODING = 'utf-8'

def saveTasks(taskModels):
	with open(file='Data.csv', mode='w', encoding=ENCODING) as taskFile:
		taskWriter = csv.writer(taskFile,
								delimiter=',',
								quotechar='"',
								quoting=csv.QUOTE_MINIMAL)
		for task in taskModels:
			taskWriter.writerow([task.Description, task.StartDate])
