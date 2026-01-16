import threading
import time


def cook_pasta():
    """Simulate cooking pasta."""
    print("Starting to boil water...")
    time.sleep(3)  # Simulating a task taking time
    print("Pasta is ready!")


def main():
    """Run multiple pasta cooking threads."""
    # Call cook_pasta once (optional)
    cook_pasta()

    # Create threads
    thread1 = threading.Thread(target=cook_pasta)
    thread2 = threading.Thread(target=cook_pasta)
    thread3 = threading.Thread(target=cook_pasta)

    # Start threads
    thread1.start()  # cook_pasta runs in the background
    thread2.start()
    thread3.start()

    # Wait for all threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    print("Dinner is served!")


if __name__ == "__main__":
    main()
