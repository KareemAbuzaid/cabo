class cabo():
	def __init__(self):
		self.t = []
		self.d = dict()

	def __setitem__(self, key, value):
		if key in self.d:
			raise ValueError("You can not ammend an existing value")
		self.d[key] = value
		self.t.append((key, value))

	def __getitem__(self, key):
		if type(key) == int:
			if key < len(self.t):
				return self.t[key]
			else:
				raise IndexError("This number is not in cabo")
		if type(key) == str:
			if self.d.get(key, False):
				return self.d[key]
			else:
				raise KeyError("This name is not in cabo")

	def __delitem__(self, key):
		raise TypeError("You can not delete an item from a cabo")	

