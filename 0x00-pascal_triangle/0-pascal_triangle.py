#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
  """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
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
