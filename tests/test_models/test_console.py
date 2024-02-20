import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
from models.base_model import BaseModel
from models._init_ import storage

class TestCreateCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_object_with_string_parameters(self, mock_stdout):
        self.console.onecmd("create BaseModel name=\"Test Object\"")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Test Object", output)
        # Verify that the object is actually created and stored
        obj_id = output.split()[3]
        obj = storage.all().get("BaseModel.{}".format(obj_id))
        self.assertIsNotNone(obj)
        self.assertEqual(obj.name, "Test Object")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_object_with_float_parameters(self, mock_stdout):
        self.console.onecmd("create BaseModel price=10.99")
        output = mock_stdout.getvalue().strip()
        self.assertIn("BaseModel", output)
        # Verify that the object is actually created and stored
        obj_id = output.split()[3]
        obj = storage.all().get("BaseModel.{}".format(obj_id))
        self.assertIsNotNone(obj)
        self.assertEqual(obj.price, 10.99)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_object_with_integer_parameters(self, mock_stdout):
        self.console.onecmd("create BaseModel quantity=5")
        output = mock_stdout.getvalue().strip()
        self.assertIn("BaseModel", output)
        # Verify that the object is actually created and stored
        obj_id = output.split()[3]
        obj = storage.all().get("BaseModel.{}".format(obj_id))
        self.assertIsNotNone(obj)
        self.assertEqual(obj.quantity, 5)

    # Add more test cases for mixed parameters, parameter validation, class name validation, etc.

if _name_ == '_main_':
    unittest.main()
