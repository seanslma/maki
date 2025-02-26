# Sparse Matrix

## diags
```py
import numpy as np
import scipy.sparse as sp
m = sp.diags([1,2,4])
```

## COO (Coordinate List) Format
The `COO` format stores a sparse matrix by recording the row and column indices of non-zero elements along with their corresponding values.

```py
# Data: non-zero values, row indices, column indices
data = np.array([4, 5, 7])
row_indices = np.array([0, 1, 2])
col_indices = np.array([0, 2, 3])

# Create COO sparse matrix
coo_matrix = sp.coo_matrix((data, (row_indices, col_indices)), shape=(4, 4))

print(coo_matrix)
```

## CSR (Compressed Sparse Row) Format 
In the `CSR` format, the matrix is stored by compressing rows into three arrays:
- `data`: The non-zero values.
- `indices`: The column indices of the non-zero values.
- `indptr`: The index pointers for the start of each row.

```py
# Data for CSR
data = np.array([4, 5, 7])
row_indices = np.array([0, 1, 2])
col_indices = np.array([0, 2, 3])

# Create CSR sparse matrix
csr_matrix = sp.csr_matrix((data, (row_indices, col_indices)), shape=(4, 4))

print(csr_matrix)
print(csr_matrix.data)    # Non-zero values
print(csr_matrix.indices) # Column indices of non-zero elements
print(csr_matrix.indptr)  # Row pointers
```

## CSC (Compressed Sparse Column) Format
Similar to the `CSR` format but optimized for column-based operations. It stores the matrix by compressing columns.

```py
# Data for CSC
data = np.array([4, 5, 7])
row_indices = np.array([0, 1, 2])
col_indices = np.array([0, 2, 3])

# Create CSC sparse matrix
csc_matrix = sp.csc_matrix((data, (row_indices, col_indices)), shape=(4, 4))

print(csc_matrix)
```

## **DOK (Dictionary of Keys) Format
The `DOK` format stores the matrix as a dictionary with keys as `(row, column)` tuples and values as the non-zero values.

```py
# Create a DOK sparse matrix
dok_matrix = sp.dok_matrix((4, 4))

# Assign values (row, column): value
dok_matrix[0, 0] = 4
dok_matrix[1, 2] = 5
dok_matrix[2, 3] = 7

print(dok_matrix)
```

## **LIL (List of Lists) Format
The `LIL` format stores each row as a list of column indices and their corresponding non-zero values.

```py
# Create a LIL sparse matrix
lil_matrix = sp.lil_matrix((4, 4))

# Assign values to the matrix
lil_matrix[0, 0] = 4
lil_matrix[1, 2] = 5
lil_matrix[2, 3] = 7

print(lil_matrix)
```

## **Dense to Sparse Conversion
```py
# Create a dense matrix
dense_matrix = np.array([
    [4, 0, 0, 0],
    [0, 0, 5, 0],
    [0, 0, 0, 7],
])

# Convert to CSR sparse matrix
csr_matrix = sp.csr_matrix(dense_matrix)

print(csr_matrix)
```

## Sparse Matrix Arithmetic
```py 
# Create two sparse matrices
A = sp.csr_matrix([[1, 0, 3], [0, 0, 0], [4, 0, 5]])
B = sp.csr_matrix([[0, 2, 0], [0, 0, 0], [1, 0, 6]])

# Matrix addition
C = A + B

print(C)
```
