from scipy.integrate import odeint
import numpy as np

class solver(object):

	def __init__(self, value=[1.0,2.0], mu = 1.0):
		self.mu = mu
		self.value = value

	def vanderpoll_derivative(self, value, t):
		x_dot = self.value[1]
		x_dot2 = self.mu * (1-self.value[0]**2) * self.value[1] - self.value[0]
		return(x_dot, x_dot2)

	def create_path(self, time = 50, frames = 500):
		x = [np.array(self.value)]
		frames = int(frames)
		for i in range(frames):
			self.value = odeint(self.vanderpoll_derivative, self.value, [0, time/frames])[1]
			x.append(self.value)
		return x

if __name__ == '__main__':
	k = solver()
	print(k.create_path())