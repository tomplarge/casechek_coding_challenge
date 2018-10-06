from flask import Flask, request, abort, Response
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

	return resource.post(data)

@app.route("/<resource>/<id>", methods=["PUT"])
def put(resource, id):
	resource = resource_from_registry(resource)
	data = request.form 

	# must have non-empty put data
	if not data:
		abort(400)

	return resource.put(id, data)

@app.route("/<resource>/<id>", methods=["DELETE"])
def delete(resource, id):
	resource = resource_from_registry(resource)

	return resource.delete(id)

def resource_from_registry(resource):
	if resource not in registry: 
		abort(404)
	else:
		return registry[resource]()
