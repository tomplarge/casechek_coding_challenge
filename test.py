import unittest
import app

from attribute import Attribute
from validations import length_equals
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

if __name__ == '__main__':
    unittest.main()