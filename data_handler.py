FILENAME = "expenses.txt"

def load_expenses():
    expenses = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                if "," in line:
                    category, amount = line.strip().split(",", 1)
                    expenses.append((category, float(amount)))
    except FileNotFoundError:
        pass
    return expenses

def save_expense(category, amount):
    with open(FILENAME, "a") as file:
        file.write(f"{category},{amount}\n")
    print(f"Saved: ${amount:.2f} for {category}")