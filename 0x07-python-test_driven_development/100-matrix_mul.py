#!/usr/bin/python3

"""
    Matrix multiplication module
"""


def matrix_mul(m_a, m_b):
    """
        function that multiplies 2 matrices
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")
    a_row_size = len(m_a[0])
    b_row_size = len(m_b[0])
    if not all(len(row) == a_row_size for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == b_row_size for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if a_row_size != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [
        [
            sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)
        ]
        for row_a in m_a
    ]

    return result
