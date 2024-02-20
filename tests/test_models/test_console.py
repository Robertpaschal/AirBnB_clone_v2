import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
from models.base_model import BaseModel
from models.__init__ import storage


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

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_object_with_updated_format(self, mock_stdout):
        self.console.onecmd(
            "create BaseModel name=\"Updated Format\" price=15.99 quantity=3")
        output = mock_stdout.getvalue().strip()
        self.assertIn("BaseModel", output)
        self.assertIn("Updated Format", output)
        self.assertIn("15.99", output)
        obj_id = output.split()[3]
        obj = storage.all().get("Basemodel.{}".format(obj_id))
        self.assertIsNotNone(obj)
        self.assertEqual(obj.name, "Updated Format")
        self.assertEqual(obj.price, 15.99)
        self.assertEqual(obj.quantity, 3)


if __name__ == '_main_':
    unittest.main()
