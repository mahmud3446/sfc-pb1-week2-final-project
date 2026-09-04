from data_handler import load_expenses, save_expense

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- ALL EXPENSES ---")
    total = 0.0
    for category, amount in expenses:
        print(f"• {category}: ${amount:.2f}")
        total += amount
    print(f"--------------------\nTOTAL SPENT: ${total:.2f}")

def add_expense():
    category = input("Enter category (e.g., Food, Gas, Rent): ").strip()
    amount_input = input("Enter amount spent ($): ").strip()

    try:
        amount = float(amount_input)
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        save_expense(category, amount)
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

def main():
    while True:
        print("\n========================")
        print("  DAILY EXPENSE TRACKER  ")
        print("========================")
        print("1. View All Expenses & Total")
        print("2. Add New Expense")
        print("3. Exit")

        choice = input("Select an option (1-3 or q): ").strip().lower()

        if choice == "1":
            view_expenses()
        elif choice == "2":
            add_expense()
        elif choice in ["3", "q", "quit", "exit"]:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()