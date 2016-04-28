class Item:
	def __init__(self, name, desc, value):
		self.name = name
		self.desc = desc
		self.value = value

	def __str__(self):
		return "Name: {}\n=========\nDescription: {}\nValue: {}".format(self.name,self.desc,self.value)

class Weapon(Item):
	def __init__(self, name, desc, value, damage):
		self.damage = damage
		super(Weapon).__init__(self, name, desc, value)

	def __str__(self):
		return "Name: {}\n=========\nDescription: {}\nValue: {}\nDoes {} damage.".format(self.name,self.desc,self.value,self.damage)
