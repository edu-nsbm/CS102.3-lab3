def main() -> None:
    while True:
        try:
            marks: float = float(input("Enter marks: "))
            break
        except ValueError:
            print("Invalid value. Retry")

    if marks >= 75:
        print("A")
    elif marks >= 60:
        print("B")
    elif marks >= 50:
        print("C")
    else:
        print("F")


if __name__ == "__main__":
    main()
