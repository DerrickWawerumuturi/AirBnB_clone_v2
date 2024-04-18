import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO;

class TestConsoleCreateCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command_string(self, mock_stdout):
        self.console.onecmd('create BaseModel name="My_house" number=123.45')
        expected_output = 'BaseModel.{}.{}\n'.format(
            self.console._last, {
                'name': 'My house',
                'number': 123.45
            }
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command_float(self, mock_stdout):
        self.console.onecmd('create BaseModel float_number=123.45')
        expected_output = 'BaseModel.{}.{}\n'.format(
            self.console._last, {
                'float_number': 123.45
            }
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command_integer(self, mock_stdout):
        self.console.onecmd('create BaseModel integer_number=123')
        expected_output = 'BaseModel.{}.{}\n'.format(
            self.console._last, {
                'integer_number': 123
            }
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command_invalid_params(self, mock_stdout):
        self.console.onecmd('create BaseModel name=My_house')  # Missing double quotes for string
        expected_output = '** invalid syntax: create BaseModel name=My_house\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
