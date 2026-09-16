import numpy.polynomial as poly

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
        y += points[i][1]/y2*y1
    return y

