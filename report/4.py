import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import lu_factor, lu_solve


def main(argv: list):
    N: int = 20
    dt: float = 1 / N

    X0: float = 0
    X20: float = 1

    alpha: float = -2.0
    beta: float = 1.0
    gamma: float = 1.0

    def delta(t: float) -> float:
        return dt**2 * (6 * t)

    # LU decomposition
    A: np.ndarray = np.zeros((N - 1, N - 1))
    for i in range(N - 1):
        A[i, i] = alpha
        if i + 1 < N - 1:
            A[i, i + 1] = gamma
            A[i + 1, i] = beta
    B: np.ndarray = np.zeros((N - 1, 1))
    for i in range(N - 1):
        if i == 0:
            B[i, 0] = delta((i + 1) * dt) - beta * X0
        elif i == N - 2:
            B[i, 0] = delta((i + 1) * dt) - gamma * X20
        else:
            B[i, 0] = delta((i + 1) * dt)

    X: np.ndarray = lu_solve(lu_factor(A), B)
    X = np.append(X0, X)
    X = np.append(X, X20)
    print(X)

    analytial_X: np.ndarray = np.zeros(N + 1)
    for t in range(0, N + 1):
        analytial_X[t] = (dt * t) ** 3

    plt.title("LU decomposition")
    plt.plot(X, label="numerical")
    plt.plot(analytial_X, label="analytical")
    plt.xlabel("t")
    plt.ylabel("X_j")
    plt.legend()
    plt.show()

    # SOR  method
    omega: float = 1.2
    epsilon: float = 1e-6


def SOR_method(A: np.ndarray, B: np.ndarray, X: np.ndarray, omega: float) -> np.ndarray:
    N: int = A.shape[0]
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i, j] = A[i, j] + omega
    return lu_solve(lu_factor(A), B)


if __name__ == "__main__":
    main(sys.argv[1:])
