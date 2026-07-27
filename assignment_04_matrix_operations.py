# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
#e M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.) TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of siz
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# Matrix Operations Program

def read_matrix(rows, cols):
    """Reads a matrix of given size from user input."""
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Row must have exactly", cols, "values.")
            exit()
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    """Displays a matrix neatly."""
    for row in matrix:
        print(" ".join(f"{val:4}" for val in row))


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)
    return transpose


def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Error: Number of columns in A must equal number of rows in B.")
        exit()

    result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result


print("=== Part A: Transpose ===")
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
matrix = read_matrix(m, n)

print("\nOriginal Matrix:")
print_matrix(matrix)

transpose = transpose_matrix(matrix)
print("\nTransposed Matrix:")
print_matrix(transpose)

print("\n=== Part B: Add Two Matrices ===")
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
print("Matrix A:")
A = read_matrix(m, n)
print("Matrix B:")
B = read_matrix(m, n)

print("\nMatrix A:")
print_matrix(A)
print("Matrix B:")
print_matrix(B)

sum_matrix = add_matrices(A, B)
print("\nSum of Matrices:")
print_matrix(sum_matrix)

print("\n=== Part C: Multiply Two Matrices ===")
m = int(input("Enter number of rows for Matrix A: "))
n = int(input("Enter number of columns for Matrix A: "))
print("Matrix A:")
A = read_matrix(m, n)

p = int(input("Enter number of columns for Matrix B: "))
print("Matrix B:")
B = read_matrix(n, p)

print("\nMatrix A:")
print_matrix(A)
print("Matrix B:")
print_matrix(B)

product = multiply_matrices(A, B)
print("\nProduct of Matrices (A × B):")
print_matrix(product)

