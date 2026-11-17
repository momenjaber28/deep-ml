import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    a=np.array(a)
    b=np.array(b)
    if (b.shape[0]!= a.shape[1]): return -1
    return np.dot(a,b)

    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    pass