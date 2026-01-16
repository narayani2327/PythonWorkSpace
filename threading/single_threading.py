import threading
import time


def cook_pasta():
    """Simulate cooking pasta."""
    print("Starting to boil water...")
    time.sleep(3)  # Simulating a task taking time
    print("Pasta is ready")


def main():
    """Main function to run the pasta cooking thread."""
    # Create the thread
    thread1 = threading.Thread(target=cook_pasta)

    # Start the thread
    thread1.start()

    # Wait for the thread to finish
    thread1.join()

    print("Dinner is served")


if __name__ == "__main__":
    main()
