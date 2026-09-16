import matplotlib.pyplot as plt
from math import sin
from newtondd import Newtondd
import numpy as np 
import numpy.polynomial as poly
import time 


x = np.linspace(-1000,1000,1000)
def f(x): 
    return x

plt.xlim(1000)
plt.ylim(1000)
plt.autoscale(False)
points = [[0,0]]
y = f(x)
graph = plt.plot(x,y)[0]
Newtdd = Newtondd(points)
while(True):
    # updating the data
    p = plt.ginput(1)[0]
    points.append(p)
    Newtdd.addpoint(p)
    f = Newtdd.get_function()
    print(f)
    y = f(x)
    graph.remove()
    
    # plotting newer graph
    graph = plt.plot(x,y,color = 'g')[0]
    
    # calling pause function for 0.25 seconds
    plt.pause(0.25)