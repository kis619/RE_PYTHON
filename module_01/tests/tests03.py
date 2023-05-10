import sys
sys.path.append('..')

from unittest import TestCase, main
from unittest.mock import patch
from io import StringIO

from ex03.load_image import load_image

class TestLoadImage(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_load_image_wrong_path(self, mock_stdout):
        self.assertEqual(load_image("wrong/path/to/image"), None)
        self.assertEqual(mock_stdout.getvalue(), "load_image: File not found\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_load_image_wrong_format(self, mock_stdout):
        self.assertEqual(load_image("module_01/tests/tests00.py"), None)
        self.assertEqual(mock_stdout.getvalue(), "load_image: Unidentified image\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_load_image_wrong_argument_type(self, mock_stdout):
        self.assertEqual(load_image(2), None)
        self.assertEqual(mock_stdout.getvalue(), "Path must be a string\n")

if __name__ == '__main__':
    main()