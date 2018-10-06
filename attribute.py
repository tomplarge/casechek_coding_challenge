from flask import abort
from validations import Validation

class Attribute:
	"""Class for resource attributes"""

	# TODO: this should really include a type
	# otherwise, filtering doesn't really work so well
	# but we're only really working with strings here, so it will work anyway
	def __init__(self, name, validations=[]):
		"""Initialize attribute for resource
		@param name(str): name of attribute
		@param validations(list(tuple)): list of validations to run, in order, for attribute value. 
			Input as list of tuples, where tuple is structured as (validation_function, list_of_args_for_func)
		"""
		self.name = name
		self.validations = []

		for validation in validations:
			validation = Validation(validation[0], validation[1])
			self.validations.append(validation)

	def validate(self, value):
		"""Validate given value against attribute validations
		@param value(any): value to validate
		@return(str || None): returns None on validation success, error message on failure
		"""
		for validation in self.validations:
			if not validation.run(value):
				error_message = "{}: {}".format(self.name, validation.error_message)
				return error_message

		return None