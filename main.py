import matplotlib.pyplot as plt
import numpy as np 
import numpy.polynomial as poly
import time 

points = [[0,1],[2,2],[3,4]]

#n^{2} And has to be revaulted every time
def lagrange_interpol_simple(points,x):
    y=0
    for i in range(len(points)):
        y1 = 1
        y2 = 1
        for j in range(len(points)):
            if i!=j:
                y1*=x-points[j][0]
                y2*=points[i][0]-points[j][0]
        y+=points[i][1]*(y1/y2)
    return y

#This time using numpy returning a polynomial the can be reused
def lagrange_interpol_numpy(points):
    y=poly.Polynomial([0]) 
    for i in range(len(points)):
        y1 = poly.Polynomial([1]) #Identiy element lol. 
        y2 = 1
        for j in range(len(points)):
            if i!=j:
                temp = poly.Polynomial([-points[j][0],1])
                y1 *= temp
                y2*=points[i][0]-points[j][0]
        y += (points[i][1]/y2)*y1
    return y





def test_func(x):
    return (0.5*(x**2))-(0.5*x)+1 

x = np.linspace(0,20,100)
yber = []
start = time.time()
for element in x:
    yber.append(lagrange_interpol_simple(points,element))
end = time.time()
plt.plot(x,yber)
start = time.time()
yfunc2 = test_func(x)
end = time.time()
funct = lagrange_interpol_numpy(points)
print(funct)
y = funct(x)
plt.plot(x,y)
plt.plot(x,yfunc2,color = 'red')
plt.show()