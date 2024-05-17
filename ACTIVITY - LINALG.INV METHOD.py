#ACTIVITY - LINALG.INV METHOD
#EXAMPLE NO.1
#Finding the inverse of a 2x2 matrix:
import numpy as np

# Define a 2x2 matrix
A = np.array([[5, 6],
              [6, 7]])

# Find the inverse of A
A_inv = np.linalg.inv(A)

print("Original Matrix A:")
print(A)
print("\nInverse of Matrix A:")
print(A_inv)


#EXAMPLE NO.2
#Solving a system of linear equations using matrix inversion:
import numpy as np

# Coefficients of the linear equations
A = np.array([[2, 1],
              [1, -1]])

# Constants
b = np.array([5, 1])

# Solve the system of linear equations Ax = b
x = np.linalg.inv(A).dot(b)

print("Solution:")
print(x)


#EXAMPLE NO.3
#Using matrix inversion to perform linear regression:
import numpy as np

# Sample data
X = np.array([[1, 1],
              [1, 2],
              [1, 3],
              [1, 4]])

y = np.array([2, 3.5, 4.5, 5.5])

# Perform linear regression using matrix inversion
theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

print("Linear regression coefficients:")
print(theta)
