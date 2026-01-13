class Model:
	def __init__(self, name, abilities, units):
		self.name = name
		self.abilities = abilities
		self.units = units

	def get_ability_string(self):
		s = ""
		for abil in self.abilities:
			s += f"{abil},"
		if s != "":
			s = s[:-1]
		return s

	def __str__(self):
		return f"Model(name={self.name}, abilities={self.get_ability_string()})"

