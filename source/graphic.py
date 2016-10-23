from vanderpol import solver
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import os

if not os.path.exists('../output'):
    os.mkdir('../output')

f = open('../input.txt',"r")
inputs = f.readlines()
a = inputs[1].split(';')
value = [0, 0]
mu, value[0], value[1], time, frames = [float(i) for i in a]

vdp_osc = solver(value, mu)
x = vdp_osc.create_path(time, frames)

cordinate, velocity = zip(*x)
fig1 = plt.figure()
mesh = np.linspace(0, time, frames+1)
plt.title("Velocity and position plot for mu = {},initial value={}".format(mu, value), fontsize=18)
plt.plot(mesh, cordinate, label = "Cordinate")
plt.plot(mesh, velocity, label = "velocity")
plt.xlabel('time')
plt.savefig("../output/position_velocity.png")

fig2 = plt.figure()
plt.plot(cordinate, velocity)
plt.title("phase plot mu = {},initial value={}".format(mu, value), fontsize=18)
plt.xlabel('time', fontsize=18)
plt.savefig("../output/phase_plot.png")

#Animation
fig = plt.figure()
plt.title("Vanderpol Oscilation animation for mu ={} and initial value ={}".format(mu, value),fontsize=18)
ax = plt.axes(xlim=(-5, 5), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)
ax.set_xlabel('x', fontsize=18)
ax.set_xlabel('y', fontsize=18)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data([0, x[i][0]], [0, 0])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
anim.save('../output/130010021_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()