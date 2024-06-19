def read_multiple_lines():
    lines = []
    print("Enter lines of text (enter an empty line to finish):")

    while True:
        line = input()
        if line == "":
            break
        else:
             lines.append(line)

    return lines


def main():
    print("You entered:")
    lines = read_multiple_lines()
    for line in lines:
        print(line)


if __name__ == '__main__':
    main()
