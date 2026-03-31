def main() -> None:
    while True:
        try:
            no_units: float = float(input("Input No of Units: "))
            break
        except ValueError:
            print("Invalid input. Retry.")

    cost: float = 0

    if no_units <= 100:
        cost = no_units * 10
    elif no_units <= 200:
        cost = 100 * 10 + (no_units - 100) * 15
    else:
        cost = 100 * 10 + 100 * 15 + (no_units - 200) * 20
   
    print(f"Bill is: {cost}")


if __name__ == "__main__":
    main()
