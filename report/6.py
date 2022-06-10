import sys

import matplotlib.pyplot as plt
import numpy as np


def Laplace_solver(N: int, k_max: int, eps: float, x_len: float, t_len: float) -> None:
    dx: float = x_len / N
    dt: float = t_len / N

    X: np.ndarray = np.linspace(0, 1, N + 1)
    for i in range(1, N + 1):
        X[i] = X[i - 1] + dx

    T: np.ndarray = np.linspace(0, 1, N + 1)
    for t in range(1, N + 1):
        T[t] = T[t - 1] + dt

    U: np.ndarray = np.zeros((N + 1, N + 1))
    for t in range(0, N + 1):
        U[0, t] = 0
        U[N, t] = 0
    for x in range(0, N + 1):
        U[x, 0] = (dx * x) * (1 - dx * x)

    k: int = 0

    while True:
        k += 1
        old_U: np.ndarray = np.copy(U)
        for x in range(1, N):
            for t in range(1, N):
                U[x, t] = (U[x, t - 1] + U[x, t + 1] + U[x - 1, t] + U[x + 1, t]) / 4
        delta: np.ndarray = np.abs(U - old_U) / U
        delta[np.isnan(delta)] = 0
        rdelta: float = delta.max()
        if rdelta < eps:
            print('r-delta:', rdelta)
            break
        if k > k_max:
            break

    for t in range(0, N + 1):
        if t * dt in [0.0, 0.25, 0.5, 0.75, 1.0]:
            plt.title("Laplace equation t = " + str(t * dt))
            plt.plot(X, U[:, t], label="t= " + str(dt * t))
            plt.xlabel("x")
            plt.ylabel(f"u(x, {dt * t})")
            plt.legend()
            plt.show()

    for x in range(0, N + 1):
        if x * dx in [0.0, 0.25, 0.5]:
            plt.title("Laplace equation x = " + str(x * dx))
            plt.plot(T, U[x, :], label="x= " + str(dx * x))
            plt.xlabel("t")
            plt.ylabel(f"u({dx * x}, t)")
            plt.legend()
            plt.show()


def main(argv: list):
    N: int = 100
    k_max: int = 10000
    eps: float = 1e-4
    Laplace_solver(N, k_max, eps, 1, 5)


if __name__ == "__main__":
    main(sys.argv[1:])
