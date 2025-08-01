# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
# my approach is:
# a = matrix
# column = len(a)
# row = len(a[0])
# go down diagonally like adding 1 to each row and column if the value after adding 1 is <= row or column respectively

#Solution using BFS to find the shortest clear path in a binary matrix.

from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    queue = deque([(0, 0, 1)])
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while queue:
        row, col, length = queue.popleft()
        
        if row == n - 1 and col == n - 1:
            return length
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < n and 0 <= c < n and not visited[r][c] and grid[r][c] == 0:
                visited[r][c] = True
                queue.append((r, c, length + 1))
    
    return -1 
