def main() -> None:
    while True:
        try:
            number: float = float(input("Enter age: "))
            break
        except ValueError:
            print("Invalid number. Retry")

    if number >= 18:
        print("Eligiable")
    else:
        print("Not eligiable")


if __name__ == "__main__":
    main()
