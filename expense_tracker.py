import json

class ExpenseTracker:
    def __init__(self, file_name="weekly_expenses.json"):
        self.file_name = file_name
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {day: 0 for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

    def save_expenses(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.expenses, file)

    def input_expenses(self):
        print("\nEnter your daily expenses:")
        for day in self.expenses:
            try:
                amount = float(input(f"{day}: "))
                self.expenses[day] += amount
            except ValueError:
                print(f"Invalid input for {day}. Skipping.")
        self.save_expenses()
        print("\nExpenses have been recorded successfully.")

    def generate_summary(self):
        total = sum(self.expenses.values())
        print("\nWeekly Expense Summary:")
        for day, amount in self.expenses.items():
            print(f"{day}: ${amount:.2f}")
        print(f"\nTotal Weekly Expenses: ${total:.2f}")

    def reset_expenses(self):
        self.expenses = {day: 0 for day in self.expenses}
        self.save_expenses()
        print("\nExpenses have been reset for the week.")


if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Input Daily Expenses")
        print("2. Generate Weekly Summary")
        print("3. Reset Weekly Expenses")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            tracker.input_expenses()
        elif choice == "2":
            tracker.generate_summary()
        elif choice == "3":
            tracker.reset_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
