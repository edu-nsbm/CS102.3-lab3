def main() -> None:
    # Conditional statements: Used when need to perform specific tasks depending on specific condition.

    # if, elif, else:
    #   if: initial confition
    #   elif: additionall condition
    #   else: if none of the above conditions are true

    input: int = -10

    if input > 0:
        print("Positive number")
    elif input == 0:
        print("Zero")
    else:
        print("Negative number")


if __name__ == "__main__":
    main()
