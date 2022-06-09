import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def Runge_Kutta_method(
    f_x, f_y, f_z, x0: float, y0: float, z0: float, dt: float, n: int
) -> tuple[list[float], list[float], list[float], list[float]]:
    """
    Runge Kutta method for numerical integration.
    :param f_x: function to integrate
    :param f_y: function to integrate
    :param f_z: function to integrate
    :param x0: initial value of x
    :param y0: initial value of y
    :param z0: initial value of z
    :param dt: time step
    :param n: number of steps
    """
    x = x0
    y = y0
    z = z0
    x_array: list[float] = [x]
    y_array: list[float] = [y]
    z_array: list[float] = [z]
    t_array: list[float] = [0]

    for _ in range(n):
        k1_x: float = f_x(x, y, z)
        k1_y: float = f_y(x, y, z)
        k1_z: float = f_z(x, y, z)

        k2_x: float = f_x(x + dt / 2 * k1_x, y + dt / 2 * k1_y, z + dt / 2 * k1_z)
        k2_y: float = f_y(x + dt / 2 * k1_x, y + dt / 2 * k1_y, z + dt / 2 * k1_z)
        k2_z: float = f_z(x + dt / 2 * k1_x, y + dt / 2 * k1_y, z + dt / 2 * k1_z)

        k3_x: float = f_x(x + dt / 2 * k2_x, y + dt / 2 * k2_y, z + dt / 2 * k2_z)
        k3_y: float = f_y(x + dt / 2 * k2_x, y + dt / 2 * k2_y, z + dt / 2 * k2_z)
        k3_z: float = f_z(x + dt / 2 * k2_x, y + dt / 2 * k2_y, z + dt / 2 * k2_z)

        k4_x: float = f_x(x + dt * k3_x, y + dt * k3_y, z + dt * k3_z)
        k4_y: float = f_y(x + dt * k3_x, y + dt * k3_y, z + dt * k3_z)
        k4_z: float = f_z(x + dt * k3_x, y + dt * k3_y, z + dt * k3_z)

        x = x + dt * (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        y = y + dt * (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        z = z + dt * (k1_z + 2 * k2_z + 2 * k3_z + k4_z) / 6

        x_array.append(x)
        y_array.append(y)
        z_array.append(z)
        t_array.append(t_array[-1] + dt)

    return x_array, y_array, z_array, t_array


def main():
    # parameters
    s, r, b = 10, 28, 8 / 3
    # initial conditions
    x0, y0, z0 = 0.2, 0.1, 0.1

    def f_x(x, y, z):
        return -s * x + s * y

    def f_y(x, y, z):
        return -x * z + r * x - y

    def f_z(x, y, z):
        return x * y - b * z

    x_array, y_array, z_array, t_array = Runge_Kutta_method(
        f_x=f_x, f_y=f_y, f_z=f_z, x0=x0, y0=y0, z0=z0, dt=0.01, n=5000
    )

    plt.plot(t_array, x_array, label="x")
    plt.title("Runge Kutta x-t")
    plt.show()

    plt.plot(t_array, y_array, label="y")
    plt.title("Runge Kutta y-t")
    plt.show()

    plt.plot(t_array, z_array, label="z")
    plt.title("Runge Kutta z-t")
    plt.show()

    ax = plt.axes(projection="3d")
    ax.set_title("Runge Kutta xyz-t")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.plot(x_array, y_array, z_array)
    plt.show()


if __name__ == "__main__":
    main()
