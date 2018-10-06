class Validation:
	def __init__(self, function, args):
		"""Initialize Validation instance. Calling run() will call provided function with provided args"""

		self.function = function
		self.args = args
		self.error_message = "Validation failed for function {} with args: {}".format(function.__name__, args)

	def run(self, value):
		"""Run validation against provided value"""

		return self.function(value, *self.args)

def length_equals(x, length):
	"""Validate length of s is equal to length

	@param x(str || list): value to validate length of
	@param length(int): length to validate against
	@return(bool): True or False
	"""

	return len(x) == length