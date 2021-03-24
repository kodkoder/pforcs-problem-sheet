# plottask.py
# This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.
#
# author: Tomasz

import matplotlib.pyplot as plt
import numpy as np

# x-Axis 0-4
xpoints = np.array(range(0,5))

# y-Axis
func_f = xpoints
func_g = xpoints * xpoints
func_h = xpoints * xpoints * xpoints

# defines plots
plt.plot(func_f, color='red')
plt.plot(func_g, color='black')
plt.plot(func_h, color='brown')

# creates labels and title
plt.title("plottask.py")
plt.xlabel("x_points")
plt.ylabel("y_points")
plt.legend()

# displays plot
plt.show()




