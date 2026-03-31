def main() -> None:
    while True:
        try:
            number: float = float(input("Enter number: "))
            break
        except ValueError:
            print("Invalid value. Retry")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    main()
