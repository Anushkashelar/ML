import numpy as np
import matplotlib.pyplot as plt

def f(x):
return (x+3)**2
def df(x):
return 2*x + 6



def gradient_descent(initial_x, learning_rate, num_iterations):
	x = initial_x
	x_history = [x]
	for i in range(num_iterations):
		gradient = df(x)
		x = x - learning_rate * gradient
		x_history.append(x)
		return x, x_history

initial_x = 2
learning_rate = 0.1
num_iterations = 50
x, x_history = gradient_descent(initial_x, learning_rate, num_iterations)
print("Local minimum: {:.2f}".format(x))
