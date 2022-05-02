
class Stack:
	def __init__(self):
		self.elements = list() 
		self.size = 0 

	#Check if stack is empty 
	def is_empty(self):
		return True if self.size == 0 else False 

	#Insert data to the stack
	def push(self, data):
		self.size += 1 
		self.elements.append(data)

	#Remove data from the stack
	def pop(self):
		self.size -= 1 
		return self.elements.pop(self.size)
