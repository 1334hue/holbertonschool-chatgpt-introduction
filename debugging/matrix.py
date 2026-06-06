#!/usr/bin/python3

def multiply_matrix_by_scalar(matrix, scalar):
    """
    Multiplies every element of a 2D matrix by a scalar.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Fix: Use matrix[i][j] instead of matrix[i][i]
            matrix[i][j] *= scalar
    return matrix

def print_matrix(matrix):
    """
    Prints the matrix in a clean format.
    """
    for row in matrix:
        print(" ".join(map(str, row)))
