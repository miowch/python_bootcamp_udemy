"""
Find PI to the Nth Digit.
Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.
"""
import math


def ask_for_digit():
    """
    Ask for digit and check whether it is positive number.
    :return: int
    """
    while True:
        user_input = str(input("Enter an amount of decimal places for PI number: "))
        try:
            if int(user_input) < 0:
                print("It should be a positive number.")
                continue
            return int(user_input)
        except ValueError:
            print("It should be a positive number.")
            continue


def generate_pi(decimal_places_amount):
    """
    Generate PI to the given digit.
    :return: str
    """
    pi = format(math.pi, f'.{decimal_places_amount}f')
    return pi


def find_pi():
    """
    Find PI up to 50 decimal places.
    :return: str
    """
    digit = ask_for_digit()
    if digit > 50:
        digit = 50
        print("Only 50 decimal places will be shown.")
    pi = generate_pi(digit)
    print(f"Pi to the {digit} digit is \n{pi}")


if __name__ == "__main__":
    find_pi()
