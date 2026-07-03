import numpy as np

def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    def derivative(a: float, b: float, c: float, x: float) -> float:
        return 2*a*x + b
    x = x0
    while(steps > 0):
        x = x - lr*derivative(a, b, c, x)
        steps-=1
    # Write code here
    return x
"""  
f(x) = ax^2 + bx + c
f'(x) = 2ax + b
"""