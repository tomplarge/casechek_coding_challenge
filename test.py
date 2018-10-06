import unittest
import app

from attribute import Attribute
from validations import length_equals
from resources import Hospital
from werkzeug.exceptions import HTTPException, NotFound

class TestAPI(unittest.TestCase):
  def test_404_invalid_resource(self):
      with self.assertRaises(HTTPException) as http_response:
          app.get_all("bad_resource")
          self.assertEqual(http_response.exception.code, 404)

class TestValidations(unittest.TestCase):
	def test_validations_run(self):
		def greater_than(n, t): return n > t
		def less_than(n, t): return n < t

		attribute = Attribute("field", validations=[(greater_than, [0]), (less_than, [2])])

		result = attribute.validate(1)

		self.assertEqual(result, None)

		result = attribute.validate(0)

		self.assertEqual(result, "field: Validation failed for function greater_than with args: [0]")

		result = attribute.validate(2)

		self.assertEqual(result, "field: Validation failed for function less_than with args: [2]")

	def test_length_equals(self):
		self.assertEqual(length_equals("foo", 3), True)
		self.assertEqual(length_equals([1,2,3], 3), True)
		self.assertEqual(length_equals("", 3), False)

class TestFilters(unittest.TestCase):
	def test_filters_work(self):
		filters = "city=Chicago"
		h1 = {'id': 1, 'name': 'Hospital 1', 'city': 'Chicago', 'state': 'IL', 'address': None}
		h2 = {'id': 2, 'name': 'Hospital 2', 'city': 'Rockford', 'state': 'IL', 'address': None}

		self.assertEqual(app.filter(Hospital(), [h1, h2], filters), [h1])

class TestCast(unittest.TestCase):
	def test_cast_works(self):
		data = (1, 'Hospital 1','Chicago', 'IL', None)
		resource = Hospital()
		expected = {'id': 1, 'name': 'Hospital 1', 'city': 'Chicago', 'state': 'IL', 'address': None}

		self.assertEqual(resource.cast(data), expected)
		
if __name__ == '__main__':
    unittest.main()