#ACTIVITY - TRANSPOSE METHOD
#EXAMPLE NO.1
#Matrix Operation: Manual Transpose
import numpy as np
matrix = [[2, 9, 13],
          [-4, 11, 17],
          [-7, 20, 12]]

transpose_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print(transpose_matrix)


#EXAMPLE NO.2
#NumPy Function: Using np.transpose()
import numpy as np

matrix = np.array([[1, -3, 5],
                   [8, 11, 10],
                   [-5, -6, 2]])

transpose_matrix = np.transpose(matrix)

print(transpose_matrix)


#EXAMPLE NO.3
#NumPy Method: Using array.T
import numpy as np

matrix = np.array([[6, -12, 23],
                   [2, 4, 6],
                   [1, -3, -5]])

transpose_matrix = matrix.T

print(transpose_matrix)

