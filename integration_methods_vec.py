from numpy import linspace, sum
from cupy import linspace as linspace_cu
from cupy import sum as sum_cu

def midpoint(f, a, b, n):
    h = (b-a)/n
    x = linspace(a + h/2, b - h/2, n)
    return h*sum(f(x))

def midpoint_cu(f, a, b, n):
    h = (b-a)/n
    x = linspace_cu(a + h/2, b - h/2, n)
    return h*sum_cu(f(x))

def trapezoidal(f, a, b, n):
    h = (b-a)/n
    x = linspace(a, b, n+1)
    s = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return h*s