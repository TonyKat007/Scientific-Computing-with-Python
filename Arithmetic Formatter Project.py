def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    for problem in problems:
        # Split the problem into its components
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        first_number, operator, second_number = parts
        
        # Validate the operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        # Validate the operands
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the result if answers are to be displayed
        if show_answers:
            if operator == "+":
                answer = str(int(first_number) + int(second_number))
            elif operator == "-":
                answer = str(int(first_number) - int(second_number))
        
        # Determine the width of the current problem
        width = max(len(first_number), len(second_number)) + 2
        
        # Construct each line with appropriate spacing
        first_line += first_number.rjust(width) + "    "
        second_line += operator + " " + second_number.rjust(width - 2) + "    "
        dashes_line += "-" * width + "    "
        
        if show_answers:
            answers_line += answer.rjust(width) + "    "
    
    # Strip the trailing spaces from each line
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    dashes_line = dashes_line.rstrip()
    if show_answers:
        answers_line = answers_line.rstrip()
    
    # Combine all lines into the final output
    if show_answers:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes_line}\n{answers_line}"
    else:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes_line}"
    
    return arranged_problems
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
