import conn
import validations
from attribute import Attribute

class Hospital:
	table = "hospitals"
	attributes = {
		"name": Attribute("name"),
		"city": Attribute("city"),
		"state": Attribute("state", validations=[(validations.length_equals, [2])]), 
		"address": Attribute("address")
	}

	def get(self, id=None):
		query = "SELECT * FROM {}".format(self.table)

		if id:
			query += " WHERE id = {}".format(id)

		return conn.execute(query, "GET")

	def post(self, data={}):
		query = "INSERT INTO {}".format(self.table)
		columns = []
		values = []

		for attr in self.attributes:
			if attr in data:
				columns.append(attr)
				values.append(data[attr])

		query += " (id"

		if columns:
			for col in columns:
				query += ", {}".format(col)

		query += ") VALUES (DEFAULT"

		if values:
			for val in values:
				query += ", '{}'".format(val)

		query += ")"

		return conn.execute(query, "POST")

	def put(self, id, data):
		query = "UPDATE {} SET".format(self.table)

		for attr in self.attributes:
			if attr in data:
				query += " {} = '{}',".format(attr, data[attr])

		query = query.rstrip(',')

		query += " WHERE id = {}".format(id)

		return conn.execute(query, "PUT")

	def delete(self, id):
		query = "DELETE FROM {} WHERE id = {}".format(self.table, id)

		return conn.execute(query, "DELETE")

	def validate(self, data):
		for attr in self.attributes:
			if attr in data:
				failed_validation = self.attributes[attr].validate(data[attr])

				if failed_validation: return failed_validation
		return None

	# def filter(self, result, filters):
	# 	"""Filter data based on filters
	# 	@param result(dict): input data, map of attribute name to value
	# 	@param filters(dict): map from attribute name to filter value
	# 	@return()
	# 	"""

	# 	fields = [attr for attr in self.attributes() if attr in result]

	# 	return[ for f in fields if filters[f] == data[f]]
