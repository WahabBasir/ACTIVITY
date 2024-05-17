#ACTIVITY - DOT METHOD
#EXAMPLE NO.1
#Using numpy.dot() function:
import numpy as np

# Define two matrices
A = np.array([[13, 26], [41, 62]])
B = np.array([[78, 33], [54, 21]])

# Calculate dot product using numpy.dot()
dot_product = np.dot(A, B)

print("Dot Product using numpy.dot():")
print(dot_product)


#EXAMPLE NO.2
#Using numpy.matmul() function:
import numpy as np

# Define two matrices
A = np.array([[10, 32], [11, 13]])
B = np.array([[54, 16], [36, 77]])

# Calculate dot product using numpy.matmul()
dot_product = np.matmul(A, B)

print("Dot Product using numpy.matmul():")
print(dot_product)


#EXAMPLE NO.3
#Using the @ operator (matrix multiplication operator)
import numpy as np

# Define two matrices
A = np.array([[21, 50], [13, 34]])
B = np.array([[52, 36], [27, 18]])

# Calculate dot product using the @ operator
dot_product = A @ B

print("Dot Product using @ operator:")
print(dot_product)
