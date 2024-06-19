def check_prefix_suffix(string, prefix, suffix):
    
    result = {
        "starts_with_prefix": string.startswith(prefix),
        "ends_with_suffix": string.endswith(suffix)
    }
    return result


def main():
    string = input("Enter a string: ")
    prefix = input("Enter a prefix to check: ")
    suffix = input("Enter a suffix to check: ")

    result = check_prefix_suffix(string, prefix, suffix)

    if result["starts_with_prefix"]:
        print(f'The string "{string}" starts with the prefix "{prefix}".')
    else:
        print(f'The string "{string}" does not start with the prefix "{prefix}".')

    if result["ends_with_suffix"]:
        print(f'The string "{string}" ends with the suffix "{suffix}".')
    else:
        print(f'The string "{string}" does not end with the suffix "{suffix}".')


if __name__ == "__main__":
    main()
