def main() -> None:
    username: str = "admin"
    password: str = "1234"

    while True:
        try:
            input_username: str = input("Enter username: ")
            input_password: str = input("Enter password: ")
            break
        except ValueError:
            print("Invalid value. Retry")

    if input_username == username and input_password == password:
        print("Welcome")
    else:
        print("Invalid credentials!")


if __name__ == "__main__":
    main()
