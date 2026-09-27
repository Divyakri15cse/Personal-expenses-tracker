import os

FILE_NAME = "expenses.txt"


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date}|{category}|{amount}|{description}\n")

    print("\nExpense added successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        print("\nNo expenses found.")
        return

    print("\n------ ALL EXPENSES ------")

    for i, line in enumerate(data, 1):
        date, category, amount, description = line.strip().split("|")

        print(f"\nExpense {i}")
        print("Date:", date)
        print("Category:", category)
        print("Amount: ₹", amount)
        print("Description:", description)


def total_expense():
    if not os.path.exists(FILE_NAME):
        print("\nTotal Expense: ₹0")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split("|")

            if len(data) == 4:
                total += float(data[2])

    print(f"\nTotal Expense: ₹{total:.2f}")


def search_expense():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    keyword = input("Enter category to search: ").lower()
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split("|")

            if keyword in category.lower():
                print(f"\nDate: {date}")
                print(f"Category: {category}")
                print(f"Amount: ₹{amount}")
                print(f"Description: {description}")
                found = True

    if not found:
        print("\nNo matching expense found.")


def delete_expenses():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        print("\nNo expenses found.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(data):
            del data[number - 1]

            with open(FILE_NAME, "w") as file:
                file.writelines(data)

            print("\nExpense deleted successfully!")
        else:
            print("\nInvalid expense number.")

    except ValueError:
        print("\nPlease enter a valid number.")


def main():
    while True:
        print("\n==============================")
        print("      PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Search Expense")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            search_expense()

        elif choice == "5":
            delete_expenses()

        elif choice == "6":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()
