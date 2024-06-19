def celsius_to_fahrenheit(celsius):

    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):

    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        print("Temperature Conversion")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Choose an option (1, 2, or 3): ")

        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius}°C")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

