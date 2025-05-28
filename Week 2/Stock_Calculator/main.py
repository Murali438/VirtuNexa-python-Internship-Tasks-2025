from calculator import add, subtract, multiply, divide
from stock_fetcher import get_stock_price
from history_manager import init_db, save_history, fetch_history

def calculator_menu():
    try:
        x = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        y = float(input("Enter second number: "))

        if op == '+':
            result = add(x, y)
        elif op == '-':
            result = subtract(x, y)
        elif op == '*':
            result = multiply(x, y)
        elif op == '/':
            result = divide(x, y)
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result}")
        save_history(f"{x} {op} {y}", result)
    except ValueError:
        print("Invalid input! Enter numeric values.")

def main():
    init_db()
    print("Welcome to the Stock Price Calculator")

    while True:
        print("\nMenu:")
        print("1. Get Stock Price")
        print("2. Calculator")
        print("3. View History")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
            price = get_stock_price(ticker)
            if price:
                print(f"{ticker} Price: ${price}")
            else:
                print("Failed to retrieve stock price.")
        elif choice == '2':
            calculator_menu()
        elif choice == '3':
            records = fetch_history()
            for rec in records:
                print(f"{rec[0]}: {rec[1]} = {rec[2]}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
