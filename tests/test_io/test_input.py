from app.io.input import read_from_file_python, read_from_file_pandas
import pandas as pd
import unittest
import os


class TestReadFromFile(unittest.TestCase):
    def test_read_existing_file(self):
        file_path = 'test_file.txt'
        expected_text = '123'
        with open(file_path, 'w') as file:
            file.write(expected_text)
        actual_text = read_from_file_python(file_path)
        self.assertEqual(actual_text, expected_text)
        os.remove(file_path)


if __name__ == '__main__':
    unittest.main()