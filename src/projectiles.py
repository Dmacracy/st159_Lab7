import numpy as np
import matplotlib.pyplot as plt 

def plot_projectile_motion(init_pos=(0,0), init_vel=(10,10), g=-9.8, time=5, timestep=0.001):
    """This function will plot the motion of a projectile in 2D space under the influence of gravity."""
    x0 = init_pos[0]
    y0 = init_pos[1]
    vel_x0 = init_vel[0]
    vel_y0 = init_vel[1]
    
    xs = []
    ys = []
    t = 0
    while t < time:
        x = x0 + vel_x0 * t
        y = max(y0 + vel_y0 * t + 0.5 * g * t**2, 0)
        xs.append(x)
        ys.append(y)
        t += timestep
    
    plt.plot(xs, ys, "r-")
    plt.title('Projectile Trajectory')
    plt.xlabel('x position (meters)')
    plt.ylabel('y position (meters)')
    plt.show()
    return xs, ys
