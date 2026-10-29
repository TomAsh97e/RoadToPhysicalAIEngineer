import numpy as np

G = 9.81

def dynamics(x, L=1.0, b=0.0):
    theta, omega = x
    return np.array([omega, -(G / L) * np.sin(theta) - b * omega])

def euler_step(f,x,dt):
    return x + dt*f(x)

def simulate(step_fn, f, x0, dt, n_steps):
    xs = np.zeros((n_steps+1, len(x0)))
    xs[0] = x0
    for i in range(n_steps):
        xs[i+1] = step_fn(f,xs[i], dt)
    return xs

def rk4_step(f, x, dt):
    k1 = f(x)
    x_mid = x+ k1*dt/2
    k2 = f(x_mid)
    x_mid2 = x + k2*dt/2
    k3 = f(x_mid2)
    k4 = f(x+k3*dt)
    return x+(dt/6)*(k1+2*k2+2*k3+k4)

def energy(xs, L=1.0):
    theta, omega  = xs[:,0], xs[:,1]
    E = 0.5 * L**2 * omega **2 - G*L*np.cos(theta)
    return E
    