import pandas as pd


def input_text():
    """Requests to input text from console.


    Returns:
        str: Entered text from user.
    """
    return input("Enter text: ")


def read_from_file_python(file_path):
    """Read data from a file.

    Args:
        file_path (str): Path to file from which data will be read.

    Returns:
        str: Text from read file.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
       """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")


def read_from_file_pandas(file_path):
    """Read data from a file using pandas.

    Args:
        file_path (str): path to file from which data will be read.

    Returns:
        pandas.DataFrame: Pandas DataFrame from read file.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
