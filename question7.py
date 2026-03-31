def main() -> None:
    number: float = float(input("Enter number: "))

    if number > 0:
        print("Positive number")
    elif number == 0:
        print("Zero")
    else:
        print("Negative number")


if __name__ == "__main__":
    main()
