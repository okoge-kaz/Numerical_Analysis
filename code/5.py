import matplotlib.pyplot as plt
import numpy as np


def func(x: float) -> float:
    return -x


def main():
    T: float = 10.0

    x_list, y_list = Euler_method(func, 0, 10, 10, T)
    plt.plot(x_list, y_list)

    x_list, y_list = Euler_method(func, 0, 10, 20, T)
    plt.plot(x_list, y_list)

    x_list, y_list = Euler_method(func, 0, 10, 100, T)
    plt.plot(x_list, y_list)
    plt.show()


def Euler_method(func, x_0: float, x_end: float, n: int, T: float) -> tuple[np.ndarray, np.ndarray]:
    dt: float = T / n

    x_list: np.ndarray = np.linspace(x_0, x_end, n)
    y_list: np.ndarray = np.zeros(n)

    y_list[0] = func(x_0)

    for index in range(1, n):
        y_list[index] = y_list[index - 1] + func(x_list[index - 1]) * (x_list[index] - x_list[index - 1])

    return x_list, y_list


if __name__ == "__main__":
    main()
