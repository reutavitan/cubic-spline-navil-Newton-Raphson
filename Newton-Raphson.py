import sympy as sp
from sympy.utilities.lambdify import lambdify


# Defining Function
def f(x):
    return x ** 3 - 5 * x - 9


# Defining derivative of function
def g(z):
    x = sp.symbols('x')
    f = x ** 3 + 2 * x + 5
    f_prime = f.diff(x)  # Derivation of  f by x
    f_prime = lambdify(x, f_prime)
    return f_prime(z)


# Implementing Newton Raphson Method
def newtonRaphson(x0, e):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        condition = abs(f(x1)) > e

    print('\nRequired root is: %0.8f' % x1)


# Input Section
# poly = input('Enter Polynomial:')
x1 = int(input('Enter start Range: '))
x2 = int(input('Enter end Range: '))
x0 = (x2 - x1) / 2

# Converting x0
x0 = float(x0)
e = float(0.00001)

# Starting Newton Raphson Method
newtonRaphson(x0, e)
