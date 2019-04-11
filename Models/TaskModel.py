import datetime

class TaskModel:
	def __init__(self, description, startDate):
		self.Description = description
		startDate = startDate.split("-")
		startDate = datetime.datetime(int(startDate[2]),
									  int(startDate[1]),
									  int(startDate[0]))
		self.StartDate = startDate

	def addEndDate(self, endDate):
		self.EndDate = endDate
		return self

	def setAllDay(self, allday):
		self.AllDay = allday
		return self

	def setImportant(self, important):
		self.Important = important
		return self

	EndDate = None
	AllDay = False
	Important = False


def addFakeData(taskModels):
	taskModels.append(TaskModel(description="Wyjazd nad morze", startDate="11-07-2019"))
	taskModels.append(TaskModel(description="Wyjście do pracy", startDate="15-03-2019"))
	taskModels.append(TaskModel(description="Wspaniałe wakacje z Karolinką nad morzem", startDate="15-03-2019"))
