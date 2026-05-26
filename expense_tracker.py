total = 0

print("=== Expense Tracker ===")
print("Enter an amount or type 'quit' to finish")

while True:
    user_input = input("\nEnter expense: ")

    if user_input == "quit":
        break

    try:
        expense = int(user_input)
        total = total + expense
        print(f"Added. Total so far: {total}")
    except ValueError:
        print("Error: enter a valid number only")

print(f"\nTotal spent: {total}")