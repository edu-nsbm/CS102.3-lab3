def main() -> None:
    while True:
        try:
            purchase_amount: float = float(input("Enter purchase amount: "))
            break
        except ValueError:
            print("Invalid value. Retry")

    final_amount: float = purchase_amount

    if purchase_amount >= 5000:
        final_amount *= 80 / 100
    elif purchase_amount >= 2000:
        final_amount *= 90 / 100

    print(f"Final amount: {final_amount}")


if __name__ == "__main__":
    main()
