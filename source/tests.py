import unittest
from vanderpol import solver

class Testsolver(unittest.TestCase):

	def setUp(self):
        	self.testing = solver()

	def testInsufficientArgs(self):
		value = [0,1]
		mu = 0.4
        self.failUnlessRaises(Exception, solver, value, mu)

if __name__=='__main__':
	unittest.main()