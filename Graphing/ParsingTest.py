from  py_expression_eval import Parser
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

equation = input("Enter an Equation (Use x and y as the variables) \n")

p = Parser()

xvals = np.arange(-10,10,0.1)

yvals = np.arange(-10,10,0.1)

zvals = []

for xi in xvals:
    for yi in yvals:
        z = p.evaluate(equation,{'x':xi , 'y':yi})
        zvals.append(z)

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.plot(xvals,yvals,1)
plt.show()
