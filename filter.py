#!/usr/bin/python3



def filter_expression(values, threshold=5.0):
    return [value for value in values if value > threshold]

if __name__ == "__main__":
    expression = [2.5, 7.1, 0.8, 5.4, 9.2, 3.0]
    result = filter_expression(expression)
    print(result)
