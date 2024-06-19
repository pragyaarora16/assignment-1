def generate_fibonacci(n):
    fibonacci_sequence = []

    if n <= 0:
        return fibonacci_sequence

    fibonacci_sequence.append(0)

    if n == 1:
        return fibonacci_sequence

    fibonacci_sequence.append(1)

    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence


def main():
    value = int(input("Enter the number"))
    fibonacci = generate_fibonacci(value)
    print(fibonacci)


if __name__ == '__main__':
    main()
