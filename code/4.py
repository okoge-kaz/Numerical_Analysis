import typing


def func(x: float) -> float:
    return x**2 - 11


def func_prime(x: float) -> float:
    return 2 * x


def main():
    x_left: float = 3.0
    x_right: float = 34.0
    epsilon: float = 1e-5  # 誤差

    # 2分法
    bisection(func, x_left, x_right, epsilon)
    # ニュートン法
    newton_method(func, func_prime, x_left, epsilon)
    # 減速ニュートン法
    decelerate_newton_method(func, func_prime, x_left, epsilon)


def bisection(func, x_left: float, x_right: float, epsilon: float) -> float:
    """
    二分法:
    args:   func: 対象関数, x_left: 左端, x_right: 右端, epsilon: 誤差
    return: 解
    """
    x_mid: float = (x_left + x_right) / 2.0
    count: int = 0

    while abs(x_right - x_left) > epsilon:
        x_mid = (x_left + x_right) / 2
        if func(x_mid) == 0:
            return x_mid
        elif func(x_mid) * func(x_left) < 0:
            x_right = x_mid
        else:
            x_left = x_mid
        count += 1
        print(f"count: {count}, left: {x_left}, right: {x_right}")
    return x_mid


def newton_method(func, func_prime, x_0: float, epsilon: float) -> float:
    """
    ニュートン法:
    args:   func: 対象関数, x_left: 左端, epsilon: 誤差
    return: 解
    """
    x_n: float = x_0 + 1
    x_b: float = x_0
    count: int = 0

    while abs(x_n - x_b) / abs(x_n) > epsilon:
        x_b = x_n  # update

        x_n = x_b - func(x_b) / func_prime(x_b)
        count += 1
        print(f"count: {count}, x: {x_n}")
    return x_n


def decelerate_newton_method(func, func_prime, x_0: float, epsilon: float) -> float:
    """
    減速ニュートン法
    """
    x_n: float = x_0 + 1
    x_b: float = x_0
    count: int = 0
    mu: float = 0.5

    while abs(x_n - x_b) / abs(x_n) > epsilon:
        x_b = x_n  # update

        x_n = x_b - mu * func(x_b) / func_prime(x_b)
        count += 1
        print(f"count: {count}, x: {x_n}")
    return x_n


if __name__ == "__main__":
    main()
