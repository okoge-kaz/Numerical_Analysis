import math

import numpy


def main():
    left_x: float = 0.0
    right_x: float = 1.0
    significant_digits: int = 4
    epsilon: float = 10 ** (-significant_digits)

    scope_x: float = right_x - left_x
    area: float = scope_x * (math.exp(left_x) + math.exp(right_x)) / 2  # 台形近似

    n: int = 1
    target_scope: float = scope_x

    while True:
        n = n * 2
        target_scope = target_scope / 2
        y_sum: float = 0.0

        for index in range(1, n // 2 + 1):
            y_sum += math.exp(left_x + (2 * index - 1) * target_scope)

        next_area: float = area / 2 + target_scope * y_sum

        # for debug
        print(f"n = {n}, area = {area}, estimated_related_error = {abs(area - next_area) / abs(area)}, related_error = {abs(next_area - (math.exp(right_x) - math.exp(left_x))) / abs(math.exp(right_x) - math.exp(left_x))}")

        if abs(next_area - area) < epsilon:
            break

        area = next_area


if __name__ == "__main__":
    main()
