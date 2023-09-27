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
    row = [0] * (i + 1)
    row[0] = 1
    row[i] = 1
    for j in range(1, i):
      row[j] = result[i - 1][j - 1] + result[i - 1][j]
    result.append(row)
  return result
