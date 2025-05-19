import time
import threading

def countdown_timer(duration_seconds):
    while duration_seconds:
        mins, secs = divmod(duration_seconds, 60)
        print(f"Time left: {mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        duration_seconds -= 1
    print("\nTime's up! ⏰")

def start_timer():
    user_input = input("Enter countdown duration (e.g., 90s or 2m): ").strip().lower()
    if user_input.endswith('s'):
        duration = int(user_input[:-1])
    elif user_input.endswith('m'):
        duration = int(user_input[:-1]) * 60
    else:
        print("Invalid input. Use 's' for seconds or 'm' for minutes.")
        return

    thread = threading.Thread(target=countdown_timer, args=(duration,))
    thread.start()
