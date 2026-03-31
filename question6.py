def main0() -> None:
    while True:
        try:
            number1: float = float(input("Enter number 1: "))
            number2: float = float(input("Enter number 2: "))
            number3: float = float(input("Enter number 3: "))
            break
        except ValueError:
            print("Invalid value. Retry")

    if number1 >= number2:
        if number1 >= number3:
            print(number1)
        else:
            print(number3)
    else:
        if number2 >= number3:
            print(number2)
        else:
            print(number3)


def main() -> None:
    while True:
        try:
            number1: float = float(input("Enter number 1"))
            number2: float = float(input("Enter number 2"))
            number3: float = float(input("Enter number 3"))
            break
        except ValueError:
            print("Invalid value. Retry")

    if number1 >= number2 and number1 >= number3:
        print(number1)
    elif number2 >= number1 and number2 >= number3:
        print(number2)
    else:
        print(number3)


if __name__ == "__main__":
    main()
