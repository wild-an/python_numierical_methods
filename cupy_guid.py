import numpy as np
import cupy as cp
import timeit
# from math import exp
from midpoint import midpoint
from integration_methods_vec import midpoint as midpoint_vec
from integration_methods_vec import midpoint_cu
from numpy import exp
from cupy import exp as exp_cu

v = lambda t: 3*t**2*exp(t**3)
v_cu = lambda t: 3*t**2*exp_cu(t**3)

# Vectorized version

t = timeit.Timer('midpoint_vec(v, 0, 3, 50000000)', setup='from __main__ import midpoint_vec, v')

time_midpoint_vec = t.timeit(10)


t = timeit.Timer('midpoint_cu(v_cu, 0, 3, 50000000)', setup='from __main__ import midpoint_cu, v_cu')

time_midpoint_cu = t.timeit(10)
# time_midpoint_cu = 1

print('Time, midpoint vec: {:g} seconds'.format(time_midpoint_vec))

print('Time, midpoint cu: {:g} seconds'.format(time_midpoint_cu))


print('Efficiency factor: {:g}'.format(time_midpoint_vec/time_midpoint_cu))


