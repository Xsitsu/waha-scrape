class Unit:
	def __init__(self, num_models, cost):
		self.num_models = num_models
		self.cost = int(cost)

	def __str__(self):
		s = ""
		if self.num_models != "1":
			s = "s"

		return f"{self.num_models} Model{s} - {self.cost} points"

