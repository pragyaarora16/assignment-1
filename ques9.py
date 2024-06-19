def check_substring(main_string, substring):
    # Check if the substring is in the main string
    if substring in main_string:
        return True
    else:
        return False


def main():
    if __name__ == "__main__":
        main_string = input("Enter the main string: ")
    substring = input("Enter the substring to check: ")

    # Check if the substring is present in the main string
    is_present = check_substring(main_string, substring)

    if is_present:
        print(f"The substring '{substring}' is present in the main string.")
    else:
        print(f"The substring '{substring}' is not present in the main string.")

if __name__ == '__main__':
    main()