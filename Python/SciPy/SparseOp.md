# Sparse Matrix Operations

## element-wise multiplication
```py
import numpy as np
import scipy.sparse as sp

# create the COO sparse matrix
data = np.array([1, 2, 3, 4])
rows = np.array([0, 1, 2, 0])
cols = np.array([0, 1, 2, 3])
m_coo = sp.coo_matrix((data, (rows, cols)), shape=(3,4))
print(m_coo.toarray())

mat = m_coo.tocsr()
vec = np.array([1,2,3,4])

# coo matrix
m1 = mat.multiply(vec)
print(f'm1 type: {type(m1)}')
print(m1.toarray())

# csr matrix: good for operation
m2 = mat.multiply(sp.csr_matrix(vec))
print(f'm2 type: {type(m2)}')
print(m2.toarray())
```
