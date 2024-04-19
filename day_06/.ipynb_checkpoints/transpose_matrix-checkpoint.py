# In the Transpose Matrix problem, we need to manipulate a matrix by reversing its rows and columns. 
# This problem is commonly used in computer science and mathematics. 
# It has many applications in areas such as image processing, linear algebra, and graph theory.

# Here’s an example of the input and output values of this problem:

#     Input: [[1,2,3],[4,5,6],[7,8,9]] | Output: [[1,4,7],[2,5,8],[3,6,9]]



def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # initializing 2d matrix
    transposed = [[0 for i in range(rows)] for j in range(cols)]

    for i in range(rows):
        for j in range(cols):
            # transpose matrix
            transposed[j][i] = matrix[i][j]

            
    return transposed


mat = [[1,2,3],[2,4,6], [1,3,5]]
print(transpose(mat))