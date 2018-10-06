import psycopg2

def execute(query, method):
	conn = psycopg2.connect("dbname=postgres")
	cursor = conn.cursor()
	cursor.execute(query)
	conn.commit()

	if method == "GET":
		result = cursor.fetchall()
	else:
		result = cursor.statusmessage

	cursor.close()
	conn.close()
	
	return "{}\n".format(result)