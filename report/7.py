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

    """result
    N = 100, I = 11.30930384461901, sigma = 55.50553638051453, s = 0.7450203781140119
    N = 100, I = 13.203696278001809, sigma = 51.385193861071144, s = 0.71683466616139
    N = 100, I = 13.048279389327767, sigma = 43.06128241553798, s = 0.6562109601000122
    N = 10000, I = 12.124924721650109, sigma = 52.19332568092976, s = 0.07224494839151716
    N = 10000, I = 12.205900511398335, sigma = 52.16983094672297, s = 0.07222868609266195
    N = 10000, I = 12.219459317699956, sigma = 52.24662707631275, s = 0.07228182833625112
    N = 1000000, I = 12.237097962320346, sigma = 51.209078903817854, s = 0.007156051907568716
    N = 1000000, I = 12.241555629536416, sigma = 51.19542308107008, s = 0.007155097698918589
    N = 1000000, I = 12.236776376803467, sigma = 51.19110396544338, s = 0.007154795871682391
    """


if __name__ == "__main__":
    main(sys.argv[1:])
