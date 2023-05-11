from unittest import TestCase, main
from module_02.ex00.load_csv import load_csv
from os import path, remove, chmod
from unittest.mock import patch
from io import StringIO
import pandas as pd
import tempfile


@patch('sys.stdout', new_callable=StringIO)
class TestLoadCsv(TestCase):
    def test_load_csv(self, _):
        self.assertIsInstance(
            # just path for unix systems
            # load_csv('module_02/population_total.csv'),

            # path with os.path.join (recommended) because it's cross-platform
            load_csv(path.join('module_02', 'population_total.csv')),
            pd.DataFrame)

    def test_load_csv_with_wrong_path(self, mock_stdout):
        self.assertIsNone(load_csv('wrong_path.csv'))
        self.assertEqual(mock_stdout.getvalue(),
                         "load_csv: File wrong_path.csv not found\n")

    def test_load_csv_with_wrong_file_type(self, mock_stdout):
        self.assertIsNone(
            load_csv(path.join('module_02', 'ex00', 'load_csv.py')))
        self.assertEqual(mock_stdout.getvalue(),
                         "load_csv: Unidentified file format\n")

    def test_load_csv_with_empty_file(self, mock_stdout):
        test_empty_file = 'test_empty_file.csv'
        with open(test_empty_file, 'w'):
            self.assertIsNone(load_csv(test_empty_file))
            self.assertEqual(mock_stdout.getvalue(),
                             "load_csv: File test_empty_file.csv is empty\n")
        remove(test_empty_file)

    def test_load_csv_no_permissions(self, mock_stdout):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            chmod(f.name, 0o200)  # remove read permission
        self.assertIsNone(load_csv(f.name))
        self.assertEqual(mock_stdout.getvalue(),
                         "load_csv: Permission denied\n")
        remove(f.name)

    def test_load_csv_unicode_decode_error(self, mock_stdout):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(b'\x80')

        self.assertIsNone(load_csv(f.name))
        self.assertEqual(mock_stdout.getvalue(),
                         f"load_csv: File {f.name} contains characters that "
                         f"cannot be decoded using the specified encoding\n")
        remove(f.name)


if __name__ == "__main__":
    main()
