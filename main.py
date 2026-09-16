import matplotlib.pyplot as plt
from math import sin
from newtondd import Newtondd
import numpy as np 
import numpy.polynomial as poly
import time 


x = np.linspace(-10,10,1000)
plt.ion()
def f(x): 
    return x

y = f(x)
graph = plt.plot(x,y)[0]
plt.show()
Newtdd = Newtondd([[0,0]])
while(True):
    # updating the data
    p = plt.ginput(1)[0]
    Newtdd.addpoint(p)
    f = Newtdd.get_function()
    print(f)
    y = f(x)
    graph.remove()
    
    # plotting newer graph
    graph = plt.plot(x,y,color = 'g')[0]
    plt.xlim(x[0], x[-1])
    
    # calling pause function for 0.25 seconds
    plt.pause(0.25)