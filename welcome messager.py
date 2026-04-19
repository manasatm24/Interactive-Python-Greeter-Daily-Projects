import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

print("=" * 50)
slow_print(" Welcome to Your Python Journey")
print("=" * 50)

name = input("\n Enter your name: ")
hobby = input(" Enter your hobby: ")

print("\nLoading your personalized message...")
time.sleep(1)

print("\n" + "=" * 50)
slow_print(f" Hello, {name}!")
slow_print(" Welcome to the world of Python programming!")
slow_print(f" It's awesome that you love {hobby}.")
slow_print(" Today is a perfect day to build something amazing!")
slow_print(" Keep learning, keep building, keep winning!")
print("=" * 50)

print("\n Let's start coding!\n")
