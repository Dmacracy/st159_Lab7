"""import two packages"""
import numpy as np
import matplotlib.pyplot as plt 

def plot_projectile_motion(init_pos=(0,0), init_vel=(10,10), g=-9.8, 
						   time=5, timestep=0.001):
	'''
	This function will plot the motion of a projectile in 2D space under the influence of gravity.
	Arguments:
		- init_pos: tuple representing the particle's initial position (inital x position, initial y position)
		- init_vel: tuple representing the particle's initial velocity (inital x velocity, initial y velocity)
		- g: gravitational acceleartion (assumed in the y direction, in meters per second squared)
		- time: total time to plot (in seconds)
		- timestep: size of timestep to use (default is 1 millisecond)
	Return values:
		- x, y: numpy arrays of the x and y position as a function of time with an entry for each time step in the 
		        whole time interval.
	'''
    x0 = init_pos[0]
    y0 = init_pos[1]
    vel_x0 = init_vel[0]
    vel_y0 = init_vel[1]
    
    xs = []
    ys = []
    t = 0
    while t < time:
        x = x0 + vel_x0 * t
        # We don't let y get below 0, so take max of simulated value and 0.
        y = max(y0 + vel_y0 * t + 0.5 * g * t**2, 0)
        xs.append(x)
        ys.append(y)
        t += timestep # increment timestep
    
    plt.plot(xs, ys, "r-")
    plt.title('Projectile Trajectory')
    plt.xlabel('x position (meters)')
    plt.ylabel('y position (meters)')
    plt.show()
    return xs, ys
