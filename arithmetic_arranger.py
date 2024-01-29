def arithmetic_arranger(problems):
    line1 = ""
    line2 = ""
    line3 = ""

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        width = max(len(operand1), len(operand2)) + 2

        lineA += operand1.rjust(width) + " "
        lineB += operator + " " + operand2.rjust(width - 2) * " "
        lineC += "-" * width + ""

    lineA = lineA.rstrip()
    lineB = lineB.rstrip()
    lineC = lineC.rstrip()

    arrangement = lineA + "\n" + lineB + "\n" + lineC

    return arrangement