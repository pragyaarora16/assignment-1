def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def main():
    if __name__ == "__main__":
        user_input = input("Enter a string to write to the file: ")

    # Define the filename
    filename = "output.txt"

    # Write the user input to the file
    write_to_file(filename, user_input)

    print(f"The string has been written to {filename}.")


if __name__ == '__main__':
    main()
