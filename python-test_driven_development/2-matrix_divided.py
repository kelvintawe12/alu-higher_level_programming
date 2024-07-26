#!/usr/bin/python3
"""
dule to divide all elements of a matrix by a divisor.

This module provides a function to divide each element of a matrix
by a given number, ensuring proper type and value checks.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and rounds the result
    to 2 decimal places.

    Parameters:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The divisor.

    Returns:
    list of lists of float: A new matrix with divided and rounded values.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats,
               or if rows in the matrix are not of the same size,
               or if div is not a number.
    ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
