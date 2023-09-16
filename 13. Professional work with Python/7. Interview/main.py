from stack import is_balanced

if __name__ == '__main__':
    expression1 = '(((([{}]))))'
    print(is_balanced(expression1))

    expression2 = '[([])((([[[]]])))]{()}'
    print(is_balanced(expression2))

    expression3 = '{{[()]}}'
    print(is_balanced(expression3))

    expression4 = '}{}'
    print(is_balanced(expression4))

    expression5 = '{{[(])]}}'
    print(is_balanced(expression5))

    expression6 = '[[{())}]'
    print(is_balanced(expression6))
