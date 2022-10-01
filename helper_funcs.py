

def evaluate_equation(equation_list):
    """
    Given a list of strings of numbers and signs, return a string of a number if valid.
    If valid, return None.
    """
    if len(equation_list) == 0:
        return 0
    elif len(equation_list) == 1:
        return equation_list[0]

    new_list = equation_list.copy()
    if equation_list[-1] in {"-", "+"}:
        new_list = new_list[:-1]
    if equation_list[0] in {"-", "+"}:
        new_list = new_list[1:]

    signs = {"+", "-"}

    current_value = int(new_list[0])
    current_op = "+" #dummy for now
    for i in range(1,len(new_list)):
        if i%2 != 0: #if odd, must be a sign
            if new_list[i] not in signs: 
                return None

            current_op = new_list[i] #for the next op
        else: #even must be a number
            if new_list[i] in signs: #if a sign, must be invalid
                return None

            if current_op == "+":
                current_value += int(new_list[i])
            elif current_op == "-":
                current_value -= int(new_list[i])
    
    return str(current_value)


# print(evaluate_equation(["1", "+", "2"]))
# print(evaluate_equation(["-","1", "+", "2"]))
# print(evaluate_equation(["-","1", "+", "2"]))
# print(evaluate_equation(["1", "-", "2"]))

