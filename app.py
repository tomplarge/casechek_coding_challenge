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

	return resource.get()

@app.route("/<resource>/<id>", methods=["GET"])
def get_one(resource, id):
	resource = resource_from_registry(resource)

	return resource.get(id)

@app.route("/<resource>", methods=["POST"])
def post(resource):
	resource = resource_from_registry(resource)
	data = request.form 

	validate(resource, data)

	return resource.post(data)

@app.route("/<resource>/<id>", methods=["PUT"])
def put(resource, id):
	resource = resource_from_registry(resource)
	data = request.form 

	if not data:
		abort(400, "PUT request must have non-empty data")

	validate(resource, data)

	return resource.put(id, data)

@app.route("/<resource>/<id>", methods=["DELETE"])
def delete(resource, id):
	resource = resource_from_registry(resource)

	return resource.delete(id)

@app.errorhandler(404)
def not_found(error):
	return build_error_response(404, error.description)

@app.errorhandler(400)
def bad_request(error):
	return build_error_response(400, error.description)

def resource_from_registry(resource):
	if resource not in registry: 
		abort(404, "No such resource: {}".format(resource))
	else: return registry[resource]()

def validate(resource, data):
	"""Run validations for resource on provided data"""
	failed_validation = resource.validate(data)
	
	if failed_validation: fabort(400, failed_validation)

def build_error_response(code, description):
	response = {
		'code': code,
		'description': description
	}

	return jsonify(response)
