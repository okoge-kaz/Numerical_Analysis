import sys

import matplotlib.pyplot as plt
import numpy as np


def leap_frog_method(f, x0: float, v0: float, dt: float, n: int) -> tuple[list[float], list[float]]:
    """
    Leap-frog method for numerical integration.
    :param f: function to integrate
    :param x0: initial value of x
    :param v0: initial value of v
    :param dt: time step
    :param n: number of steps
    :return: x(n+1) and v(n+1)
    """
    x = x0
    v = v0
    x_array: list[float] = [x]
    v_array: list[float] = [v]

    for i in range(n):
        if i == 0:
            v = v + dt * f(x)
            v_array.append(v)
        else:
            if i % 2 == 1:
                x = x + 2 * dt * v
                x_array.append(x)
            else:
                v = v + 2 * dt * f(x)
                v_array.append(v)
    return x_array, v_array


def Heun_method(f, x0: float, v0: float, dt: float, n: int) -> tuple[list[float], list[float]]:
    """
    Heun method for numerical integration.
    :param f: function to integrate
    :param x0: initial value of x
    :param v0: initial value of v
    :param dt: time step
    :param n: number of steps
    :return: x(n+1) and v(n+1)
    """
    x = x0
    v = v0
    x_array: list[float] = [x]
    v_array: list[float] = [v]

    for i in range(n):
        k1: float = f(x)
        k2: float = f(x + dt * k1)
        x = x + dt * v
        v = v + dt * (k1 + k2) / 2
        x_array.append(x)
        v_array.append(v)
    return x_array, v_array


def main(argv: list):
    def f(x: float):
        return -x

    x_array, v_array = leap_frog_method(f, 1, 0, 0.01, 1000)
    plt.plot(x_array, v_array, label="xv-LF")
    plt.show()

    x_array, v_array = Heun_method(f, 1, 0, 0.01, 1000)
    plt.plot(x_array, v_array, label="xv-Heun")
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
