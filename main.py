import random
import itertools
import time


def random_equation_generator():
    number_of_operators = random.randint(2,4)
    operators = ["*", "-", "/", "+"]
    numbers = random.choices(range(0, 101), k=number_of_operators + 1)
    chosen_operators = random.choices(operators, k=number_of_operators)
    random_equation = ''.join(str(num) + op for num, op in zip(numbers, chosen_operators))  # Create the equation by interleaving numbers and operators
    random_equation += str(numbers[-1])  # Add the last number without an operator
    return random_equation


def wrong_answer_displayer(wrong_answer_dict):
    print("---------------------------------------------")
    print("The correct answers to the questions you answered wrong or skipped:")
    for key in wrong_answer_dict.keys():
        if wrong_answer_dict[key][1] == "Answer skipped":
            print(f"{key} = {wrong_answer_dict[key][0]:.2f} -> You skipped this answer!\n")
        else:
            print(f"{key} = {wrong_answer_dict[key][0]:.2f} -> Your answer is {wrong_answer_dict[key][1]}, which is incorrect!\n")


def is_numeric_input(inp_value):
    try:
        float(inp_value)
        return True
    except ValueError:
        return False


def main():
    quit_or_not = True
    while quit_or_not:
        correct_answers = 0  # Counter for correct answers
        wrong_answered_equations = {}  # Container for wrong answered expressions
        n = 0  # Number of equations generated, which will not update in case of ZeroDivisionError
        start_time = time.time()  # Start timer
        while n < 10:  # Loop to generate 10 expressions
            numbers = random_equation_generator()
            expression = ''.join(str(item) for item in numbers)  # Create expression from the list "numbers"
            try:
                result = round(eval(expression), 2)  # Compute the result of each expression
                n += 1
            except ZeroDivisionError:
                continue
            inp_result = input(f"Enter the result of the equation or press enter to skip "
                                   f"(2 floating point approximation):\n{expression} = ")  # Ask the user its answer
            while True:
                if inp_result == "":  # If user skipped the question
                    wrong_answered_equations[expression] = (result, "Answer skipped")
                    break
                elif not is_numeric_input(inp_result):
                    inp_result = input(f"Please enter a number: \n{expression} = ")  # If not, ask again

                elif isinstance(eval(inp_result), float) or isinstance(eval(inp_result),int):  # Check if the input is of the right type
                    if float(inp_result) == float(result):  # Check if the input answer is right
                        correct_answers += 1  # Update the number of right answers
                    else:
                        wrong_answered_equations[expression] = (result, inp_result) # Update the container for wrong answered expressions
                    break

        end_time = time.time()  # Stop timer
        total_elapsed_time = end_time - start_time  # Compute total time
        wrong_answer_displayer(wrong_answered_equations)
        print(f"Total elapsed time: {total_elapsed_time:.2f} seconds\n") # Write total time
        print(f"Total score: {correct_answers}/10 = {100 * correct_answers/10:.2f}%\n")  # Write total score as fraction and percentage
        quit_option = input("Press 0 to Quit the test,\n"
                            "Press anything else to continue: ")
        # Let's assume quit_option is defined elsewhere and is a string input from the user
        if quit_option.isdigit():  # Check if the input is all digits
            if int(quit_option) == 0:  # Quit if the input is 0
                quit_or_not = False
                print("Thanks for playing!")
            else:
                quit_or_not = True  # Keep playing if the input is any other number
        else:
            quit_or_not = True  # This covers cases where the input is not numeric
            

if __name__ == "__main__":
    main()
