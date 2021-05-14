import numpy as np


def knapsack(v, w, W):
    # Initialize variables
    n = len(v)  # The amount of values we can fill knapsack with.
    K = np.zeros((W + 1, n + 1), dtype=int)  # 2D array filled with zeros.

    # Update the values in the K array
    for i in range(1, n + 1):
        for x in range(1, W + 1):
            K[x][i] = K[x, i - 1]
            if w[i - 1] <= x:
                K[x][i] = max(K[x][i], K[x - w[i - 1]][i - 1] + v[i - 1])

    return K[W][n]


v = [20, 5, 10, 40, 15, 25]
w = [1, 2, 3, 8, 7, 4]
W = 10
print("Knapsack value is", knapsack(v, w, W))

