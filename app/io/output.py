def print_to_console(*args, **kwargs):
    """Prints text to the console.

    Args:
        *args: Positional arguments to be printed to the console.
        **kwargs: Keyword arguments that can be used to configure the printing.

    Returns:
        None
    """
    print(*args, **kwargs)


def write_to_file( data, file_path):
    """Writes data to a file.

    Args:
        data (str): The data to write to the file.
        file_path (str): The path to the Python file to write.

    Returns:
        None

    Raises:
        IOError: If an error occurs while writing to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except IOError:
        raise IOError("Error writing to file")


def write_to_file_pandas(dataframe, file_path):
    """
    Writes a pandas DataFrame to a file.

    Args:
        dataframe (pandas.DataFrame): The DataFrame to write to the file.
        file_path (str): The path to the file where the DataFrame will be written.

    Returns:
        None

    Raises:
        IOError: If an error occurs while writing to the file.
    """
    try:
        dataframe.to_csv(file_path)
    except IOError:
        raise IOError("Error writing to file")

