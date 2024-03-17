from app.io.input import read_from_file_python, read_from_file_pandas
import pandas as pd
import unittest
import os


class TestReadFromFile(unittest.TestCase):
    def test_read_existing_file(self):  # Checks if expected equals result
        file_path = 'test_file.txt'
        expected_text = '123'
        with open(file_path, 'w') as file:
            file.write(expected_text)
        actual_text = read_from_file_python(file_path)
        self.assertEqual(actual_text, expected_text)
        os.remove(file_path)

    def test_read_nonexistent_file(self):  # Checks if FileNotFoundError called
        file_path = 'nonexistent_file.txt'
        with self.assertRaises(FileNotFoundError):
            read_from_file_python(file_path)

    def test_read_empty_file(self):   # Checks if read text is empty
        file_path = 'empty_file.txt'
        open(file_path, 'a').close()
        actual_text = read_from_file_python(file_path)
        self.assertEqual(actual_text, '')
        os.remove(file_path)

    def test_read_existing_file_pandas(self):  # Checks if starting DataFrame equals result
        data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        df = pd.DataFrame(data)
        file_path = 'test_file.csv'
        df.to_csv(file_path, index=False)
        df_read = read_from_file_pandas(file_path)
        pd.testing.assert_frame_equal(df_read, df)
        os.remove(file_path)

    def test_read_nonexistent_file_pandas(self):  # Checks if FileNotFoundError called
        file_path = 'nonexistent_file.csv'
        with self.assertRaises(FileNotFoundError):
            read_from_file_pandas(file_path)

    def test_return_type_pandas(self):  # Checks if return DataFrame
        file_path = 'test_file.csv'
        data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        result = read_from_file_pandas(file_path)
        self.assertIsInstance(result, pd.DataFrame)
        os.remove(file_path)


if __name__ == '__main__':
    unittest.main()