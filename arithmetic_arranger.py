def arithmetic_arranger(problems):
    line1 = ""
    line2 = ""
    line3 = ""

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        width = max(len(operand1), len(operand2)) + 2

        line1 += operand1.rjust(width) + " "
        line2 += operator + " " + operand2.rjust(width - 2) * " "
        line3 += "-" * width + ""
