def sum_of_numbers(number):
    return sum(number)


def main():
    input_string = input("Enter a list of numbers separated by spaces: ")
    number = list(map(float, input_string.split()))
    result = sum_of_numbers(number)
    print("The sum of the numbers is:", result)

if __name__ == '__main__':
    main()
