import sys

import numpy as np


def Monte_Carlo_method(N: int, x_len: float, y_len: float, z_len: float) -> None:
    Z = np.zeros(N)
    sum: float = 0.0

    for i in range(0, N):
        x = np.random.uniform(0, x_len)
        y = np.random.uniform(0, y_len)
        if (x / 4) ** 2 + (y / 3) ** 2 < 1:
            # 8は対照性より 0<= x && 0 <= y && 0 <= z となるようにしている
            Z[i] = 8 * np.sqrt(4 - 4 * (x / 4) ** 2 + 4 * (y / 3) ** 2)
            sum += Z[i]

    I: float = sum / N
    var: float = 0.0
    for i in range(0, N):
        var += (Z[i] - I) ** 2

    var = var / (N - 1)
    dI = np.sqrt(var / N)
    print(f"N = {N}, I = {I}, sigma = {var}, s = {dI}")


def main(argv: list):
    x_len: float = 4.0
    y_len: float = 3.0
    z_len: float = 2.0
    for _ in range(3):
        Monte_Carlo_method(100, x_len, y_len, z_len)
    for _ in range(3):
        Monte_Carlo_method(10000, x_len, y_len, z_len)
    for _ in range(3):
        Monte_Carlo_method(1000000, x_len, y_len, z_len)


if __name__ == "__main__":
    main(sys.argv[1:])
