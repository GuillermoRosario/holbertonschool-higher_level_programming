#!/usr/bin/python3
# Write a function that computes the square value of 
# all integers of a matrix.

def square_matrix_simple(matrix=[]):
    def square(matrix):
        new_matrix = []
        for row in matrix:
            new_matrix.append(row*row)
        return new_matrix
    return list(map(square, matrix))
