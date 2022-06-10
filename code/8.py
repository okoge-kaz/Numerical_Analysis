import numpy as np


def main():
    pass


def Gauss_Elimination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    n: int = A.shape[0]
    x: np.ndarray = np.zeros(n)

    # Forward Elimination 前進消去
    for k in range(n - 1):
        for i in range(k + 1, n):
            if A[i, k] != 0:
                lam: float = A[i, k] / A[k, k]
                A[i, k + 1 : n] = A[i, k + 1 : n] - lam * A[k, k + 1 : n]
                b[i] = b[i] - lam * b[k]

    # Backward Substitution 後退代入
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1 : n], x[i + 1 : n])) / A[i, i]

    return x


if __name__ == "__main__":
    main()
