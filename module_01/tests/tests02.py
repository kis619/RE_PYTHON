import sys
sys.path.append("..")

from ex02.load_image import ft_load
from unittest import TestCase, main
from unittest.mock import patch
from io import StringIO

def my_function():
    print("Hello, world!")

class TestFtLoad(TestCase):
    
    # The @patch('sys.stdout', new_callable=StringIO) decorator
    # is used to replace the standard output with a StringIO object,
    # which allows us to capture the output of the print() function
    @patch('sys.stdout', new_callable=StringIO)
    def test_ft_load_file_not_found(self, mock_stdout):
        self.assertEqual(ft_load("not_found.png"), None)
        self.assertEqual(mock_stdout.getvalue(), "File at path not_found.png not found\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_ft_load_unsupported_image_format(self, mock_stdout):
        self.assertEqual(ft_load("module_01/normal-level.webp"), None)
        self.assertEqual(mock_stdout.getvalue(), "Image format: WEBP\nUnsupported file format\n")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_ft_load_unsupported_file_format(self, mock_stdout):
        self.assertEqual(ft_load("module_01/tests/tests00.py"), None)
        self.assertEqual(mock_stdout.getvalue(), "Unidentified image\n")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_ft_load_argument_not_string(self, mock_stdout):
        self.assertEqual(ft_load(2), None)
        self.assertEqual(mock_stdout.getvalue(), "Path must be a string\n")

    def test_ft_load_shape(self):
        self.assertEqual(ft_load("module_01/landscape.jpg").shape, (257, 450, 3))
        
if __name__ == "__main__":
    main()