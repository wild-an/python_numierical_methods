from typing import Callable

def trapezoidal(f:Callable, a:float, b:float,n:int ) -> float:
    # inteval to calcualte trapezoids 
    dh = (b-a)/n
    trapez_val = [] # values of are of trapez
    trapez_val.extend([.5*f(a), .5*f(b)])
    for i in range(1, n):
        trapez_val.append(f(a+i*dh))
    
    return sum(trapez_val)*dh

if __name__ == '__main__':
    from math import exp
    v = lambda t: 3*(t**2)*exp(t**3)
    n = 4
    print(trapezoidal(v, 0, 1, n) - 1.9227167504675762)