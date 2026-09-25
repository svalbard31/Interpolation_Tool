import random as rand
from newtondd import Newtondd
from lagrange import lagrange_interpol_numpy
import numpy as np
import matplotlib.pyplot as plt
import time

def create_random_points(linspace, y_range=(-1000, 1000)):
    """Creates random points within the given x and y ranges."""
    points = []
    for i in linspace:
        x = i
        y = rand.uniform(*y_range)
        points.append([x, y])
    return points

def speed_test(num_points, x_range=(-1000, 1000), y_range=(-1000, 1000)):
    """Tests the speed of Newton's divided difference and Lagrange interpolation."""
    linspace = np.linspace(x_range[0], x_range[1], num_points)
    points = create_random_points(linspace, y_range)

    # Test Newton's divided difference
    start_time = time.time()
    newton = Newtondd(points)
    newton_time = time.time() - start_time

    # Test Lagrange interpolation
    start_time = time.time()
    lagrange = lagrange_interpol_numpy(points)
    lagrange_time = time.time() - start_time

    #Test adding a point to Newton's divided difference
    new_point = [rand.uniform(*x_range), rand.uniform(*y_range)]
    start_time = time.time()
    newton.addpoint(new_point)
    newton_addpoint = time.time() - start_time
    return newton_time, lagrange_time, newton_addpoint

def run_speed_tests(max_points=100, min_points=2, step=2):
    """Runs speed tests for increasing number of points."""
    results = []
    for num_points in range(min_points, max_points + 1, step):
        newton_time, lagrange_time, newton_addpoint = speed_test(num_points)
        results.append((num_points, newton_time, lagrange_time, newton_addpoint))
        print(f"Points: {num_points}, Newton Time: {newton_time:.6f}s, Lagrange Time: {lagrange_time:.6f}s, Newton Add Point Time: {newton_addpoint:.6f}s")
    return results

def get_plot_data(results):
    """Prepares data for plotting."""
    num_points = [result[0] for result in results]
    newton_times = [result[1] for result in results]
    lagrange_times = [result[2] for result in results]
    newton_addpoint_times = [result[3] for result in results]
    return num_points, newton_times, lagrange_times, newton_addpoint_times

results = run_speed_tests(100)
plot_data = get_plot_data(results)

plt.plot(plot_data[0], plot_data[1], label='Newton\'s Divided Difference', color='blue')
plt.plot(plot_data[0], plot_data[2], label='Lagrange Interpolation', color='orange')
plt.plot(plot_data[0], plot_data[3], label='Newton Add Point', color='green')
plt.xlabel('Number of Points')
plt.ylabel('Time (seconds)')
plt.title('Speed Comparison of Interpolation Methods')
plt.legend()
plt.show()

