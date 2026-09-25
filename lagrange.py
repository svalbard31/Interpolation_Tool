import numpy.polynomial as poly

#First version of lagrange interpolation
def lagrange_interpol_simple(points,x):
    """Returns the value of the lagrange interpolation polynomial at x given a list of points"""
    y=0 
    for i in range(len(points)):
        y1 = 1
        y2 = 1
        for j in range(len(points)):
            if i!=j:
                y1*=x-points[j][0]
                y2*=points[i][0]-points[j][0]
        y+=points[i][1]*(y1/y2)
    return y #returns an evalution of the polynomial at x.

#Uses Numpy and returns a polynomial object.
def lagrange_interpol_numpy(points):
    """Returns a polynomial object that is the lagrange interpolation of the given points"""
    y=poly.Polynomial([0]) #A 0 polynomial to add to.
    for i in range(len(points)): #Runs n times
        y1 = poly.Polynomial([1]) 
        y2 = 1
        #Creates the top line of the polynomial
        for j in range(len(points)):#Runs n*n times
            if i!=j:
                temp = poly.Polynomial([-points[j][0],1])
                y1 *= temp
                y2*=points[i][0]-points[j][0]
        y += points[i][1]/y2*y1 #calutes the portion of the polynomial and adds it to the whole polynomial.
    return y

