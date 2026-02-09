import math

def add(a, b):
    # Adds to numbers together and returns the result
    return a + b

def sub(a, b):
    # Subtracts the second number from the first and returns the result
    return a - b

def mul(a, b):
    # Multiple two numbers and return the result
    return a * b

def div(a, b):
    # divides the first number by the second ensuring second number != 0 and returns result
    if b == 0:
        return float('inf')  
    return a / b

def log(value, base):
    return math.log(value, base)

def log10(value):
    return math.log(value)