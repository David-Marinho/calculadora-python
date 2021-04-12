def calculadora(n1, n2, op):
    result = 0

    if op == '+':
        result = n1 + n2

    elif op == '-':
        result = n1 - n2

    elif op == '*':
        result = n1 * n2

    elif op == '/':
        result = n1 / n2

    elif op == '%':
        result = n1 % n2

    elif op == 'r':
        result = n1 ** (1/n2)

    return result
