
class Node:
	def __init__(self):
		print("Contructor called")
		self.data = 0

	def setData(self, d):
		self.data = d

	def print(self):
		print("Data: ", self.data)

	def __str__(self):
		return "I don't like classes"





a = Node()
a.setData(10)
a.print()