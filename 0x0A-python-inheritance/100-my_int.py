#!/usr/bin/python3
"""
    class MyInt module
"""


class MyInt(int):
    """
        class MyInt that inherits from int
    """
    def __eq__(self, x):
        """initialization of eq"""

        return not super().__eq__(x)

    def __ne__(self, x):
        """initialization for greater than"""

        return not super().__ne__(x)
