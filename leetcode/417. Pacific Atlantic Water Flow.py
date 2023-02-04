from typing import List


def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
  rows, cols = len(heights), len(heights[0])
  pacific, atlantic = set(), set()

  def dfs(row, col, visited, prevHeight):
    if (row, col) in visited or row < 0 or col < 0 or row == rows or col == cols or heights[row][col] < prevHeight:
      return

    visited.add((row,col))

    dfs(row+1, col, visited, heights[row][col])
    dfs(row-1, col, visited, heights[row][col])
    dfs(row, col+1, visited, heights[row][col])
    dfs(row, col-1, visited, heights[row][col])

  for col in range(cols):
    dfs(0, col, pacific, heights[0][col])
    dfs(rows-1, col, atlantic, heights[rows-1][col])

  for row in range(rows):
    dfs(row, 0, pacific, heights[row][0])
    dfs(row, cols-1, atlantic, heights[row][cols-1])

  result = []
  for row in range(rows):
    for col in range(cols):
      if (row, col) in atlantic and (row, col) in pacific:
        result.append([row, col])

  return result