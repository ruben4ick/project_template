from app.io.input import input_text, read_from_file_python, read_from_file_pandas
from app.io.output import print_to_console, write_to_file, write_to_file_pandas


def main():
    # Console input and output
    text = input_text()
    print_to_console(text)

    # Python reading and writing
    file_path = "data/example.txt"
    data_to_write = "Testing functions"
    write_to_file(data_to_write, file_path)
    data_from_file = read_from_file_python(file_path)
    print_to_console(data_from_file)

    # Pandas functions
    file_path_csv = "data/example.csv"
    data_from_csv = read_from_file_pandas(file_path_csv)
    print_to_console("Data from example.csv using pandas:")
    print_to_console(data_from_csv)
    write_to = "data/write_to.csv"
    write_to_file_pandas(data_from_csv, write_to)


if __name__ == '__main__':
    main()