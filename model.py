class Model:
	def __init__(self, name, units):
		self.name = name
		self.units = units

	def __str__(self):
		return f"Model(name={self.name})"

