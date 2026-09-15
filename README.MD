# MAT-2201 Uit 2026 Task: E; Interpolation Engine
This is a work in progress interpolation demo. 
## Task overview 
### 1 
Implement three ways to evaluate the interpolating polynomial: the Lagrange form (3.1) directly;
the Newton form via newtdd + nest; and the Newton form with incremental updating, where
adding one point adds one divided-difference row (Example 3.4). Checkpoint 1: reproduce
Examples 3.1–3.6 with all three and check that they agree to machine precision.

### 2
Count operations. For n nodes and m evaluation points, how many multiplications does each
method need? Fill in a table for n = 5, 10, 50 and m = 1000, then measure actual timings and
compare with your counts.

### 3 
Real-time updating: build the click-to-add tool. Adding the k-th point must reuse the previous k−1
rows of the divided-difference table. Demonstrate it live.

### 4 
Exercises 3.1.7–3.1.10 and 3.1.13 look like heavy computations, but each has a one-line answer if
you use the right idea. Present one of them as a puzzle to the audience.

### 5 
Accuracy: interpolate eˣ at n = 10, 20, 40 Chebyshev nodes and evaluate with the Lagrange form
and the Newton form. Are the answers equal? Look at the size of the divided differences and of
the Lagrange basis polynomials Lₖ. Which form is more sensitive to rounding, and where?