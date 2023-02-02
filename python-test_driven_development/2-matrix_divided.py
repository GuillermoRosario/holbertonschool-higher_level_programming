#!/usr/bin/python3
def matrix_divided(matrix, div):
    def divide(matrix):
        new_matrix = []
        for row in matrix:
            new_matrix.append(round(row / div, 2))
        return new_matrix
        if new_matrix != int and float:
            raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
        if div != float and int:
            raise TypeError ("Each row of the matrix must have the same size")
    return list(map(divide, matrix))