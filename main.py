from store import Store
from cli import CLI

store = Store()
cli = CLI(store)

while True:
    print("MINISTORE")
    print("1.Manager")
    print("2.Customer")
    print("3.Exit")

    choice = input("choice an option:")

    if choice == "1":
        result = cli.manager_menu()

        if result == "exit":
            continue

    elif choice == "2":
        result = cli.customer_menu()

        if result == "main":
            continue

    elif choice == "3":
        break

    else:
        print("invalid choice")