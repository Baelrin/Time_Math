import time
import random

OPERATORS = [
    "+",
    "-",  # List of operators used in problems
    "*",
]
MIN_OPERAND = 3  # Minimum value for operands
MAX_OPERAND = 12  # Maximum value for operands
TOTAL_PROBLEMS = 10  # Total number of problems to be solved


def generate_problem():
    """
    Generates a mathematical problem using random operands and operators.

    Returns:
        tuple: Contains a string representation of the problem and its integer answer.
    """
    left = random.randint(MIN_OPERAND, MAX_OPERAND)  # Random left operand
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # Random right operand
    operator = random.choice(OPERATORS)  # Random operator from the list

    expr = f"{left} {operator} {right}"  # String expression of the problem
    answer = eval(expr)  # Calculates the correct answer
    return expr, answer


def get_user_input(expr):
    """
    Continuously prompts the user to solve the given expression until a valid integer is entered.

    Args:
        expr (str): The expression the user needs to solve.

    Returns:
        int: The user's guessed answer.
    """
    while True:
        try:
            guess = input(f"Problem: {expr} = ")  # Ask for user input
            return int(guess)  # Return the integer guess
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handles non-integer inputs


def main():
    """
    Main function that executes the math problem challenge.
    It tracks user time and number of incorrect answers.
    """
    wrong = 0  # Counter for wrong answers
    input("Press enter to start!")  # Initial prompt to start the game
    print("----------------------")

    start_time = time.time()  # Start time tracking

    for _ in range(TOTAL_PROBLEMS):  # Loop through a fixed number of problems
        expr, answer = generate_problem()  # Generate a new problem
        user_answer = get_user_input(expr)  # Get the user's answer
        if user_answer == answer:  # Check if the user's answer is correct
            print("Correct.")
        else:
            print("Incorrect.")
            wrong += 1  # Increment wrong counter if the answer is incorrect

    end_time = time.time()  # Stop time tracking
    total_time = round(end_time - start_time, 2)  # Calculate total time taken

    print("----------------------")
    print(
        f"You finished in {total_time} seconds with {wrong} wrong answers."
    )  # Display the results


if __name__ == "__main__":
    main()  # Entry point for the program