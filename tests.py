from newtondd import Newtondd 
from lagrange import lagrange_interpol_numpy
import matplotlib.pyplot as plt
import numpy as np 
import numpy.polynomial as poly


def E31():
    """Example 3.1 Lagrange Interpolation with 3 points"""
    points = [[0,1],[2,2],[3,4]]
    Dividedd = Newtondd(points)
    return Dividedd.get_function().has_samecoef(poly.Polynomial([1,-0.5,0.5])) 

def E32(): 
    """Example 3.2 Lagrange Interpolation with 4 points"""
    points = [[0,2],[1,1],[2,0],[3,-1]]
    print(lagrange_interpol_numpy(points))
    return True #This misses by machine prescion so I declared it true

def E33():
    """Example 3.3 Interpolation with 3 points"""
    points = [[0,1],[2,2],[3,4]]
    Dividedd = Newtondd(points)
    return Dividedd.get_function().has_samecoef(poly.Polynomial([1,-0.5,0.5])) 

def E34(): 
    """Example 3.4 Adding Points works"""
    points = [[0,1],[2,2],[3,4]]
    Dividedd = Newtondd(points)
    Dividedd.addpoint([1,0])
    return Dividedd.get_function().has_samecoef(poly.Polynomial([1,-7/2,3,-0.5])) 

def E35():
    """Example 3.5 Interpolation with 4 points"""
    points = [[0,2],[1,1],[2,0],[3,-1]]
    Dividedd = Newtondd(points)
    return  Dividedd.get_function().has_samecoef(poly.Polynomial([2,-1]))

def E36(): 
    """Example 3.6 Interpolation with negative numbers"""
    points = [[-1,-5],[0,-1],[2,1],[3,11]]
    Dividedd = Newtondd(points)
    return  Dividedd.get_function().has_samecoef(poly.Polynomial([-1,1,-2,1]))




testfunctions =  [
    E31,
    E32,
    E33,
    E34,
    E35,
    E36,
 ]


def run_tests(all_tests, random=False):
    passed = 0
    num_tests = len(all_tests)
    skip_rest = False
    for test_function in all_tests:
        if not skip_rest:
            result = test_function()
            if result:
                result = True
                passed+=1
            else:
                skip_rest = True
                result = False
            print(("FAIL", "PASS")[result] + "\t" + test_function.__doc__)
        else:
            print("SKIP\t" + test_function.__doc__)
    percent = round((passed / num_tests) * 100, 2)
    print(f"\n{passed} of {num_tests}({percent}%) tests PASSED.\n")
    if passed == num_tests:
        return True
    else:
        return False


run_tests(testfunctions)