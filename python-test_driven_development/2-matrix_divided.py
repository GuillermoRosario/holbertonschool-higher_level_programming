#!/usr/bin/python3
def matrix_divided(matrix, div):
    def divide(matrix):
        new_matrix = []
        for row in matrix:
            new_matrix.append(round(row / div, 2))
        return new_matrix
    return list(map(divide, matrix))
