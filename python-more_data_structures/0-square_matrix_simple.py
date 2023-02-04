#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def alados(matrix):
        new_matrix = []
        for row in matrix:
            new_matrix.append(row * row)
        return new_matrix

    return list(map(alados, matrix))
