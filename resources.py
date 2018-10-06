import conn

class Hospital:
	table = "hospitals"
	attributes = ["name", "city", "state", "address"]

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
