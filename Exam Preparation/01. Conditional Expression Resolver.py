def parse_expression(expression, idx):
    if expression[idx].isdigit():
        return expression[idx]

    if expression[idx] == 't':
        return parse_expression(expression, idx + 2)

    cursor = idx + 2
    conditional_statements_counter = 0
    while True:
        symbol = expression[cursor]
        if symbol == '?':
            conditional_statements_counter += 1
        elif symbol == ':':
            if conditional_statements_counter == 0:
                return parse_expression(expression, cursor + 1)
            conditional_statements_counter -= 1
        cursor += 1

expression = input().split()
print(parse_expression(expression, 0))
