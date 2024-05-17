#ACTIVITY - LINALG.DET METHOD
#EXAMPLE NO.1
#Calculate determinant of a 2x2 matrix:
import numpy as np

# Define a 2x2 matrix
matrix_2x2 = np.array([[1, 3],
                       [5, 7]])

# Calculate determinant
det_2x2 = np.linalg.det(matrix_2x2)

print("Determinant of 2x2 matrix:")
print(det_2x2)


#EXAMPLE N0.2
#Calculate determinant of a 3x3 matrix:
import numpy as np

# Define a 3x3 matrix
matrix_3x3 = np.array([[2, 4, 6],
                       [8, 10, 12],
                       [16, 18, 20]])

# Calculate determinant
det_3x3 = np.linalg.det(matrix_3x3)

print("Determinant of 3x3 matrix:")
print(det_3x3)


#EXAMPLE NO.3
#Calculate determinant of a randomly generated square matrix:
import numpy as np

# Generate a random 4x4 matrix
matrix_4x4 = np.random.rand(4, 4)

# Calculate determinant
det_4x4 = np.linalg.det(matrix_4x4)

print("Determinant of randomly generated 4x4 matrix:")
print(det_4x4)
