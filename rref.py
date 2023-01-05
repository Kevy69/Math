# import sympy 
from sympy import * 
  
M = Matrix([[1, -1, -1, 0],
            [1, 1, -2, 1],
            [-1, 2, 4, -3]])
print("Matrix : {} ".format(M))

# Use sympy.rref() method 
M_rref = M.rref()

print("Row echelon form (w pivots): {}".format(M_rref))