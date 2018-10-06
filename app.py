from flask import Flask, request, abort, Response, jsonify
from resources import Hospital

app = Flask(__name__)

registry = {
	"hospitals": Hospital
}

@app.route("/", methods=["GET"])
def index():
  return "Casechek Coding Challenge API v1.0\n"

@app.route("/<resource>", methods=["GET"])
def get_all(resource):
	resource = resource_from_registry(resource)

	results = resource.get()

	response = []

	for r in results:
		response.append(resource.cast(r))

	filters = request.args.get('filter')

	if filters: 
		response = filter(resource, response, filters)

	return build_response(200, response)

@app.route("/<resource>/<id>", methods=["GET"])
def get_one(resource, id):
	resource = resource_from_registry(resource)

	result =  resource.get(id)

	response = resource.cast(result[0])

	return build_response(200, response)

@app.route("/<resource>", methods=["POST"])
def post(resource):
	resource = resource_from_registry(resource)
	data = request.form 

	validate(resource, data)

	result = resource.post(data)

	return build_response(201, result)

@app.route("/<resource>/<id>", methods=["PUT"])
def put(resource, id):
	resource = resource_from_registry(resource)
	data = request.form 

	if not data:
		abort(400, "PUT request must have non-empty data")

	validate(resource, data)

	result =  resource.put(id, data)

	return build_response(202, result)

@app.route("/<resource>/<id>", methods=["DELETE"])
def delete(resource, id):
	resource = resource_from_registry(resource)

	result =  resource.delete(id)

	return build_response(202, result)

@app.errorhandler(404)
def not_found(error):
	return build_response(404, error.description)

@app.errorhandler(400)
def bad_request(error):
	return build_response(400, error.description)

def resource_from_registry(resource):
	if resource not in registry: 
		abort(404, "No such resource: {}".format(resource))
	else: return registry[resource]()

def validate(resource, data):
	"""Run validations for resource on provided data"""
	failed_validation = resource.validate(data)
	
	if failed_validation: abort(400, failed_validation)

def filter(resource, results, input_filters):
	try:
		filters = parse_filters(input_filters)

		return resource.filter(results, filters)
	except:
		abort(400, "Filters in URL not formatted properly: {}".format(input_filters))

def build_response(code, message):
	response = {
		'code': code,
		'message': "{}".format(message)
	}

	return jsonify(response)

def parse_filters(filters):
	filters = filters.split(",")
	result = {}

	for f in filters:
		f = f.split("=")
		result[f[0]] = f[1]

	return result