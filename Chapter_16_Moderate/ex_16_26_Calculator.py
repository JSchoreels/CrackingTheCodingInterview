def eval_factor(repr, start, end): # start and end inclusive
    result = 1
    prev_operator = ''
    current_number = ''
    for i in range(start, end+1):
        if repr[i].isdigit():
            current_number += repr[i]
        if repr[i] in ('*', '/'):
            current_number = int(current_number)
            if prev_operator == '':
                result *= current_number
            elif prev_operator == '*':
                result *= current_number
            elif prev_operator == "/":
                result /= current_number
            else:
                raise ValueError("Code desync between condition and mappings")
            prev_operator = repr[i]
            current_number = ''
    current_number = int(current_number)
    if prev_operator == '':
        result *= current_number
    elif prev_operator == '*':
        result *= current_number
    elif prev_operator == "/":
        result /= current_number
    print(f"Result of {repr[start:end+1]} : {result}")
    return result


def calculator(repr):
    assert len(repr) > 0
    result = None
    last_operator = None
    i_start_term = 0
    len(repr) - 1
    for i in range(len(repr)):
        if repr[i] == '+' or repr[i] == '-':
            i_end_term = i - 1
            term_to_eval = eval_factor(repr, i_start_term, i_end_term)
            if not result:
                result = term_to_eval
            if last_operator == '+':
                result += term_to_eval
            elif last_operator == '-':
                result -= term_to_eval
            last_operator = repr[i]
            i_start_term = i + 1
    last_term_to_eval = eval_factor(repr, i_start_term, len(repr) - 1)
    if last_operator == '+':
        result += last_term_to_eval
    elif last_operator == '-':
        result -= last_term_to_eval
    return result

print(calculator("2*3+5/6*3+5"))
print(calculator("2*3+5/6*3+15"))