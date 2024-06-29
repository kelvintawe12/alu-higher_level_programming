#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    square_matrix_map = lambda m: [list(map(lambda x: x ** 2, row)) for row in m]
