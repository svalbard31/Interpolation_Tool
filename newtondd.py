import matplotlib.pyplot as plt
import numpy as np 
import numpy.polynomial as poly
import time 

class Newtondd: 
    """Class for Newton's divided difference interpolation"""
    def __init__(self,points):
        """Initializes the class and calculates the divided difference table and the polynomial function"""
        data = self._pointsto_xy(points)
        self.xdata = data[0]
        self.ydata = data[1]
        self.interpolated = []
        self.function = poly.Polynomial([0])
        self.interpolated = self.interpolate()
        self.function = self.interpret()

    def _pointsto_xy(self,points): 
        """Converts a list of points to two lists of x and y values"""
        xdata = []
        ydata = []
        for point in points: 
            xdata.append(point[0])
            ydata.append(point[1])
        return xdata, ydata

    def interpolate(self):
        """Calculates the divided difference table and returns it as a list of lists"""
        interpolated= [self.ydata] 
        colum = self.ydata
        counter = 1 
        while len(colum)>1: 
            temp = []
            for i in range((len(colum)-1)):
                temp.append((colum[i+1]-colum[i])/(self.xdata[i+counter]-self.xdata[i]))
            counter +=1
            colum = temp
            interpolated.append(temp)
        self.interpolated = self.interpolated
        return interpolated    
    def interpret(self): 
        """Calculates the polynomial function from the divided difference table and returns it as a polynomial object"""
        function = poly.Polynomial([0])
        count = 0
        for i in self.interpolated: #n times
            polypart = poly.Polynomial([i[0]])
            temp = poly.Polynomial([1])
            for j in range(count): #n*n times
                temp*=poly.Polynomial([-self.xdata[j],1])
            count+=1
            polypart *= temp
            function+=polypart
        self.function = function
        return function
    

    def addpoint(self,point):
        """Adds a point to the interpolation and recalculates the divided difference table and polynomial function"""
        temp = point[1]
        if point[0] in self.xdata: 
            print("points can't have same x value")
            return
        for i in range(len(self.interpolated)): # n times 
            prevtemp = temp
            #print(f"{temp}-{self.interpolated[i][-1]}/{point[0]}-{self.xdata[-1-i]}")
            temp = (temp-self.interpolated[i][-1])/(point[0]-self.xdata[-1-i])
            self.interpolated[i].append(prevtemp)
        self.interpolated.append([temp])
        self.function = self.interpret()
        self.xdata.append(point[0])
        self.ydata.append(point[1])
        return self.function
    def printinterpolated(self):
        #print the divided difference by collums
        for i in self.interpolated: 
            print(i)
        
    def deletepoint(self,point): 
        for i in range(self.xdata): 
            if self.xdata == point[0] and self.ydata == point[1]: 
                self.xdata.pop(i)
                self.ydata.pop(i)
        self.interpolated = self.interpolate()
        self.function = self.interpret()
        return self.function

    def get_function(self): 
        return self.function




    
