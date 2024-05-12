cpdef int factorial_cython(int n):
    """
    Cythonized version of the factorial function with types added.
    """
    cdef int result = 1
    cdef int i
    for i in range(1, n + 1):
        result *= i
    return result