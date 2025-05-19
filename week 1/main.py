from timer import start_timer
from calculator import perform_operation
from logger import log_to_file
from db import init_db, save_to_db

def main():
    init_db()  # Only if using SQLite

    while True:
        print("\nChoose an option:")
        print("1. Start Countdown Timer")
        print("2. Calculator")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            start_timer()
        elif choice == '2':
            result = perform_operation()
            if result:
                log_to_file(result)
                save_to_db(result)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
