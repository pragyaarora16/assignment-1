def main():
    num = int(input("Enter a number"))
    sum_num = 0
    while num > 0:
        sum_num = sum_num + num % 10
        num = num//10

    print(sum_num)


if __name__ == '__main__':
    main()
