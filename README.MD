# MAT-2201 Uit 2026 Task: E; Interpolation Engine
This is an interpolation Demo, with three parts
## Requriments 
The project is written in python
The following external libraies are used, matplotlib, numpy, sympy
If you don't have them use 
```
pip install matplotlib &
pip install numpy &
pip install sympy
```
## Parts 
### Part 1 : Tests
This is implemented in the file Tests.py.
It creates a testing framework based on examples from the book (Numerical Anyalsis Second Edtion)
There are 7 tests in total, 5 suceed and 2 fail. 
The two that fail are because of rounding errors, both of the failures are smaller e-16. 
### Part 2: Click To Interpolate
This program allows the user to click to add points to an interpolation. 
It uses Newton Divided Diffrence interpolation, and does not recalulate the entire table when adding points. 
Instead using the method provided in the book, to reuse previous rows of the table

### Part 3: Rounding Errors and Chebysev Nodes 
Found in Node.py. This program interpolates at e^x at Chebysev nodes for n=10, n=20, n=40. 
It uses both lagrange and Newton interpolation. 
It calculates and prints the errors for easy review and comparison, 
### 4
Exercises 3.1.7–3.1.10 and 3.1.13 look like heavy computations, but each has a one-line answer if
you use the right idea. Present one of them as a puzzle to the audience.

### 5 
Accuracy: interpolate eˣ at n = 10, 20, 40 Chebyshev nodes and evaluate with the Lagrange form
and the Newton form. Are the answers equal? Look at the size of the divided differences and of
the Lagrange basis polynomials Lₖ. Which form is more sensitive to rounding, and where?