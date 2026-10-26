m = 1
k = 1
f = 0
v = 0

#Euler Method
def step_Euler(x,u,dt):
    f = -k*x
    a = f / m
    v = u + a*dt
    x1 = x + v*dt

    return x1, v

#RK4
def step_RK4(x,u,dt):
    K = []
    f = -k*x
    a = f / m

    #k1
    k1x = u
    k1v = -x
    K.append((k1x, k1v))

    #k2
    x_spot = x + k1x*(dt/2)
    v_spot = u + k1v*(dt/2)
    k2x = v_spot
    k2v = -x_spot
    K.append((k2x, k2v))

    #k3
    x_spot = x + k2x*(dt/2)
    v_spot = u + k2v*(dt/2)
    k3x = v_spot
    k3v = -x_spot
    K.append((k3x, k3v))

    #k4
    x_spot = x + k3x*(dt)
    v_spot = u + k3v*(dt)
    k4x = v_spot
    k4v = -x_spot
    K.append((k4x, k4v))

    x_spot = (K[0][0] + 2*K[1][0] + 2*K[2][0] + K[3][0])/6
    v_spot = (K[0][1] + 2*K[1][1] + 2*K[2][1] + K[3][1])/6

    x1 = x + x_spot*dt
    v = u + v_spot*dt

    return x1, v

if __name__ == "__main__":
    print(step_RK4(1, 0, 0.1))