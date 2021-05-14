import numpy as np


def knapsack(v, w, W):
    # Initialize variables
    n = len(v)  # The amount of values we can fill knapsack with.
    K = np.zeros((W + 1, n + 1), dtype=int)  # 2D array filled with zeros. Extra row and column to include weight 0
    # and no values

    # Update the values in the K array
    for i in range(1, n + 1):  # i is the ith value available.
        for weight in range(1, W + 1):
            kvalue_without_weight = K[weight][i - 1]
            kvalue_including_weight = K[weight - w[i - 1]][i - 1] + v[i - 1] if w[i - 1] <= weight else K[weight, i - 1]
            K[weight][i] = max(kvalue_without_weight, kvalue_including_weight)
    return K[W][n]


v = [20, 5, 10, 40, 15, 25]
w = [1, 2, 3, 8, 7, 4]
W = 10
print("Knapsack value is", knapsack(v, w, W))

