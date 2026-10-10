m = 1
k = 1
f = 0
v = 0
i=0

#Euler Method
def step_forward(x,u,dt):
    f = -k*x
    a = f / m
    v = u + a*dt
    x1 = x + v*dt

    return x1, v

x = 1
v = 0
dt = 0.1
while i < 63:
    x, v = step_forward(x, v, 0.1)
    print(x,v)
    i += 1
