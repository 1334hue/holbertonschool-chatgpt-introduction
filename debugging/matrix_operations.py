#!/usr/bin/python3
"""
Module Description:
This module provides utility functions for handling matrix operations,
specifically focusing on printing 2D grids and multiplying matrix
elements by a numerical scalar.
"""

def print_matrix(matrix):
    """
    Function Description:
    Prints a 2D matrix row by row with space-separated elements.

    Parameters:
    matrix (list of list of int/float): The 2D matrix grid to be printed.

    Returns:
    None
    """
    for row in matrix:
        print(" ".join(map(str, row)))


def multiply_matrix_by_scalar(matrix, scalar):
    """
    Function Description:
    Multiplies all entries inside a 2D matrix by a given scalar factor.

    Parameters:
    matrix (list of list of int/float): The matrix to scale.
    scalar (int/float): The multiplier value.

    Returns:
    list of list of int/float: The modified matrix with scaled values.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= scalar
    return matrix
