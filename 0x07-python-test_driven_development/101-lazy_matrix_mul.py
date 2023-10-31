#!/usr/bin/python3

"""
    matrix multiplication using the module NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        function that multiplies 2 matrices
    """

    result = np.dot(m_a, m_b)
    return result
