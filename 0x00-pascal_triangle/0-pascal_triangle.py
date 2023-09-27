#!/usr/bin/python3

"""
0-pascal_triangle
"""

def pascal_triangle(n):
  """Returns a list of lists of integers representing the Pascal's triangle of n.

  Returns an empty list if n <= 0.

  Args:
    n: The number of rows in the Pascal's triangle.

  Returns:
    A list of lists of integers representing the Pascal's triangle of n.
  """
    
    if n <= 0:
        return []
    result = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(result[i - 1]) - 1):
            curr = result[i - 1]
            temp.append(result[i - 1][j] + result[i - 1][j + 1])
        temp.append(1)
        result.append(temp)
    return result
