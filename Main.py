import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def lorenz_attractor(dt, num_steps, sigma=10, rho=28, beta=8/3, start_point=(-8, 8, 27)):
    xs, ys, zs = [start_point[0]], [start_point[1]], [start_point[2]]
    x, y, z = start_point
    for i in range(num_steps):
        x_dot = sigma * (y - x)
        y_dot = x * (rho - z) - y
        z_dot = x * y - beta * z
        x += x_dot * dt
        y += y_dot * dt
        z += z_dot * dt
        xs.append(x)
        ys.append(y)
        zs.append(z)
    return xs, ys, zs

# Initial conditions and parameters
dt = 0.01
num_steps = 10000

# Calculating the points in the Lorenz attractor
xs, ys, zs = lorenz_attractor(dt, num_steps)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

graph, = ax.plot(xs, ys, zs, lw=0.5)

# Update function for the animation
def update(n):
    graph.set_data(xs[:n], ys[:n])
    graph.set_3d_properties(zs[:n])
    return graph,

# Creating the animation
ani = FuncAnimation(fig, update, frames=len(xs), interval=30)

plt.show()
