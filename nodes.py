
import math
from lagrange import lagrange_interpol_numpy
from newtondd import Newtondd
import sympy as sp
from sympy.abc import x
import numpy as np

def chebyshev_nodes(a,b,n): 
    """
    This function takes two the borders of a range and returns n chebyshev nodes in that range.
    """
    nodes = []
    for i in range(n): 
        node = (((b-a)/2)*math.cos(((2*i+1)*math.pi)/(2*n)))+((b+a)/2)
        nodes.append(node)
    return nodes

def f(x):
    """Function to be interpolated""" 
    return math.e**x

def evaluate_at_nodes(nodes): 
    """Evaluates the function at the given nodes"""
    points = []
    for node in nodes:
        points.append([node,f(node)])
    return points
#print(chebyshev_nodes(-1,1,10))
#print(evaluate_at_nodes(chebyshev_nodes(-1,1,10)))

def interpolation_test(test_sizes): 
    """Tests the interpolation function"""
    evaluation_n = []
    evaluation_l = []
    for n in test_sizes:
        nodes = chebyshev_nodes(-1,1,n)
        nodes = evaluate_at_nodes(nodes)
        lagrange = lagrange_interpol_numpy(nodes)
        newton = Newtondd(nodes)
        newton_function = newton.get_function()
        evaluation_n.append(newton_function)
        evaluation_l.append(lagrange)

    return evaluation_n, evaluation_l

interpolation_results = interpolation_test([10,20,40])

def print_pretty_polynomial(poly): 
    """Prints the polynomial in a pretty format"""
    sp.init_printing()
    return sp.Poly(reversed(poly.coef),x).as_expr()

for i in interpolation_results[0]:
    sp.pprint(sp.pretty(print_pretty_polynomial(i)))
    print("\n\n")

def evaulate_error(interpolation_results): 
    """Evaluates the error of the interpolation"""
    errors = []
    for i in range(len(interpolation_results[0])):
        newton = interpolation_results[0][i]
        lagrange = interpolation_results[1][i]
        error_l = []
        error_n = []

        for x in np.linspace(-1,1,10000):
            error_l.append(abs(lagrange(x)-f(x)))
            error_n.append(abs(newton(x)-(f(x))))
        errors.append((error_l, error_n))
    return errors

errors = evaulate_error(interpolation_results)
print(f"At 10 nodes: \n Max error newton: {max(errors[0][1])} \n Max error lagrange: {max(errors[0][0])}\n min error newton: {min(errors[0][1])} \n min error lagrange: {min(errors[0][0])}\n avg error newton: {sum(errors[0][1])/len(errors[0][1])} \n avg error lagrange: {sum(errors[0][0])/len(errors[0][0])}\n")
print(f"At 20 nodes: \n Max error newton: {max(errors[1][1])} \n Max error lagrange: {max(errors[1][0])}\n min error newton: {min(errors[1][1])} \n min error lagrange: {min(errors[1][0])}\n avg error newton: {sum(errors[1][1])/len(errors[1][1])} \n avg error lagrange: {sum(errors[1][0])/len(errors[1][0])}\n")
print(f"At 40 nodes: \n Max error newton: {max(errors[2][1])} \n Max error lagrange: {max(errors[2][0])}\n min error newton: {min(errors[2][1])} \n min error lagrange: {min(errors[2][0])}\n avg error newton: {sum(errors[2][1])/len(errors[2][1])} \n avg error lagrange: {sum(errors[2][0])/len(errors[2][0])}\n")
