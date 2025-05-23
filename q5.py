# -*- coding: utf-8 -*-
"""q5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18RUJ-gyyU6TTFmLPLKFD79WmSyBtllw0
"""

OK_FORMAT = False
name = "q5"

import math

def least_common_multiple(a, b):
    """
    Returns the least common multiple of two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: The LCM of a and b.
    """
    return abs(a*b) // math.gcd(a, b)  # Calculate and return the LCM