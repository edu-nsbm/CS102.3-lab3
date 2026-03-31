def main():
    while True:
        try:
            acc_balance: float = float(
                input("Enter account balance (ex: 5000000.00): ")
            )
            withdrawal_amount: float = float(
                input("Enter withdrawal amount (ex: 50000.00): ")
            )
            break
        except ValueError:
            print("Invalid value. Retry.")

    if acc_balance >= 500.00:
        if withdrawal_amount <= acc_balance - 500:
            acc_balance -= withdrawal_amount
            print(f"Withdrawal successful. Remaining balance: {acc_balance}")
        else:
            print("Insufficient balance")
    else:
        print("Cannot withdraw. Minimum balance of 500 required")


if __name__ == "__main__":
    main()
