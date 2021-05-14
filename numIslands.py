from collections import defaultdict

LAND = '1'
WATER = '0'


def numIslands(grid):
    """
    Finds the number of islands found on a grid. An island is surrounded by water and is formed by connecting adjacent
    lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    :param grid: an m x n 2D binary matrix grid which represents a map of '1's (land) and '0's (water).
    :return: the number of islands.

    Example:
    Input: grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
    ]
    Output: 3
    """
    count = 0
    explored = defaultdict(lambda: False)
    for m in range(len(grid)):
        for n in range(len(grid[m])):
            if not explored[(m, n)] and grid[m][n] == LAND:
                explore_island(grid, (m, n), explored)
                count += 1
    return count


def explore_island(grid, initial, explored):
    """
    Marks all positions which form part of the island as explored. Explores the island using DFS

    :param grid: The grid with the representation of the islands.
    :param initial: The position from which the exploration begins
    :param explored: A dictionary mapping each position to True if explored or False if not explored.
    """
    stack = [initial]
    while len(stack) > 0:
        m, n = stack.pop()

        # Explore north
        if m - 1 >= 0 and grid[m-1][n] != WATER and not explored[(m-1, n)]:
            stack.append((m-1, n))

        # Explore south
        if m + 1 < len(grid) and grid[m+1][n] != WATER and not explored[(m+1, n)]:
            stack.append((m+1, n))

        # Explore east
        if n + 1 < len(grid[m]) and grid[m][n+1] != WATER and not explored[(m, n+1)]:
            stack.append((m, n+1))

        # Explore west
        if n - 1 >= 0 and grid[m][n-1] != WATER and not explored[(m, n-1)]:
            stack.append((m, n-1))

        explored[(m, n)] = True


grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]
print(numIslands(grid))
