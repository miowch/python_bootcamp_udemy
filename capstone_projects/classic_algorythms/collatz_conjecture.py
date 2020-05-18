"""
Start with a number n > 1.
Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1.
"""


def ask_number():
    while True:
        user_input = input("Please provide a number > 1: ")
        try:
            number = int(user_input)
            if number <= 1:
                print("Number should be more than 1.")
                continue
            return number
        except ValueError:
            print("Please provide an integer.")
            continue


def count_steps_to_one(number):
    step = 0

    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        step += 1

    return step


def collatz_conjecture():
    number = ask_number()
    steps = count_steps_to_one(number)
    print(f"It takes {steps} steps to reach 1. ")


if __name__ == '__main__':
    collatz_conjecture()
