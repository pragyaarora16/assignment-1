def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")


def main():
    file_path = input("Enter the path to the text file: ")

    read_and_print_file(file_path)


if __name__ == '__main__':
    main()
