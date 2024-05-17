#ACTIVITY - FLATTEN METHOD
#EXAMPLE NO.1
#Using NumPy's flatten method:
import numpy as np

# Define a 2D array
matrix = np.array([[11, 23, -9],
                   [10, 15, 5],
                   [-7, 8, 4]])

# Flatten the matrix using flatten method
flattened_matrix = matrix.flatten()
print(flattened_matrix)


#EXAMPLE NO.2
#Using NumPy's reshape method:
import numpy as np

# Define a 2D array
matrix = np.array([[-1, 7, 5],
                   [9, 15, 21],
                   [17, 2, -9]])

# Reshape the matrix into a single row
flattened_matrix = matrix.reshape(1, -1)
print(flattened_matrix)


#EXAMPLE NO.3
#Using matrix multiplication:
import numpy as np

# Define a 2D array
matrix = np.array([[8, -5, 12],
                   [10, 16, 19],
                   [-7, 11, 10]])

# Create a column vector of ones
ones_vector = np.ones(matrix.shape[1])

# Flatten the matrix by matrix multiplication
flattened_matrix = np.dot(matrix, ones_vector)
print(flattened_matrix)
