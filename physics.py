m = 1
k = 1
f = 0
v = 0

#Euler Method
def step_forward(x,u,dt):
    f = -k*x
    a = f / m
    v = u + a*dt
    x1 = x + v*dt

    return x1, v