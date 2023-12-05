# Write python program that user to enter only odd numbers, else will raise an exception.

def odd():
    while True:
        try:
            n = int(input("Enter an odd number: "))
            if n % 2 != 1:
                raise ValueError("Entered number is not odd.")
            return n
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter an odd number.")

# Example usage
try:
    n = odd()
    print(f"You entered an odd number : {n}")
except Exception as e:
    print(f"An error occurred: {e}")


