class TaskModel:
	def __init__(self, description, startDate):
		self.Description = description
		self.StartDate = startDate
	EndDate = None
	AllDay = False
	Important = False
