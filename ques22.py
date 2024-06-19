def find_min_max(numbers):
    min_value = numbers[0]
    max_value = numbers[0]


    for num in numbers:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return min_value,max_value

print(f"The minimum value is: {min_value}")
print(f"The maximum value is: {max_value}")
