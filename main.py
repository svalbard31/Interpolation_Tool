import matplotlib.pyplot as plt
import numpy as np 
import numpy.polynomial as poly
import time 


points = [[0,1],[2,2],[3,4]]

def pointsto_xy(points): 
    xdata = []
    ydata = []
    for point in points: 
        xdata.append(point[0])
        ydata.append(point[1])
    return xdata, ydata

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


#Newton Divided Difference Calculate Table
def newtondd(xdata,ydata): 
    interpolated= [ydata] 
    colum = ydata
    counter = 1 
    while len(colum)>1: 
        temp = []
        for i in range((len(colum)-1)): 
            temp.append((colum[i+1]-colum[i])/(xdata[i+counter]-xdata[i]))
        counter +=1
        colum = temp
        interpolated.append(temp)
    return interpolated

#Netwon divided diffrence create polynomial
def netwoninterpret(interpolated,xdata): 
    function = poly.Polynomial([0])
    count = 0
    for i in interpolated: 
        polypart = poly.Polynomial([i[0]])
        temp = poly.Polynomial([1])
        for j in range(count): 
            temp*=poly.Polynomial([-xdata[j],1])
        count+=1
        polypart *= temp
        function+=polypart
    return function

#Newton divided diffrence add point
def newtonaddpoint(point,interpol,xdata):
    temp = point[1]
    for i in range(len(interpol)):
        prevtemp = temp
        print(f"({temp}-{interpo[i][-1]})/({point[0]}-{xdata[-1-i]})")
        temp = (temp-interpo[i][-1])/(point[0]-xdata[-1-i])
        interpol[i].append(prevtemp)
    interpol.append([temp])
    return interpol

    
    pass


pointsxy = pointsto_xy(points)
interpo = newtondd(pointsxy[0],pointsxy[1])
print(newtonaddpoint([1,0],interpo.copy(),pointsxy[0]))
f = netwoninterpret(interpo,pointsxy[0])
print(f)


#Correct function to compare against
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
ynewtdd = f(x)
plt.plot(x,y)
plt.plot(x,yfunc2,color = 'red')
plt.plot(x,ynewtdd)
plt.show()