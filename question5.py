def main() -> None:

    while True:
        try:
            number1: float = float(input("Enter number 1: "))
            number2: float = float(input("Enter number 2: "))
            break
        except ValueError:
            print("Invalid input. Retry")

    if number1 >= number2:
        print(f"Larger number is: {number1}")
    else:
        print(f"Larger number is: {number2}")


if __name__ == "__main__":
    main()
