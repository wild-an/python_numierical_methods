
def double_midpoint(f, a, b, c, d, nx, ny):
    running_sum = 0
    hx = (b - a)/nx
    hy = (d- c)/ny
    I = 0
    for i in range(nx):
        x_i = a + hx/2 + i*hx
        for j in range(ny):
            y_j = c + hy/2 + i*hy
            
    return running_sum

