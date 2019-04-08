class TaskModel:
	def __init__(self, description, startDate):
		self.Description = description
		self.StartDate = startDate
	EndDate = None
	AllDay = False
	Important = False


def addFakeData(taskModels):
	taskModels.append(TaskModel(description="Wyjazd nad morze", startDate="11-07-2019"))
	taskModels.append(TaskModel(description="Wyjście do pracy", startDate="15-03-2019"))
	taskModels.append(TaskModel(description="Wspaniałe wakacje z Karolinką nad morzem", startDate="15-03-2019"))
