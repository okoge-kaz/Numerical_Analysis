import sys
from statistics import variance

import numpy as np
import pandas as pd


def main(argv: list):
    CSV_DATA: pd.DataFrame = pd.read_csv("data/5_data.csv")
    X: np.ndarray = np.array(CSV_DATA["X"])
    Y: np.ndarray = np.array(CSV_DATA["Y"])
    XY: np.ndarray = X * Y
    dY: np.ndarray = np.array(CSV_DATA["dY"])

    weighted_x_mean: np.float64 = np.sum(X / (dY) ** 2) / np.sum(1 / (dY) ** 2)
    weighted_y_mean: np.float64 = np.sum(Y / (dY) ** 2) / np.sum(1 / (dY) ** 2)
    weighted_xy_mean: np.float64 = np.sum(XY / (dY) ** 2) / np.sum(1 / (dY) ** 2)
    weighted_xx_mean: np.float64 = np.sum(X**2 / (dY) ** 2) / np.sum(1 / (dY) ** 2)
    weight_sum: np.float64 = np.sum(1 / (dY) ** 2)
    # print(1 / (dY) ** 2)
    print("weighted_x_mean:", weighted_x_mean)
    print("weighted_y_mean:", weighted_y_mean)

    print("XY:", XY)

    variance_weighted_x: np.float64 = np.sum((X - weighted_x_mean) ** 2 / (dY) ** 2) / weight_sum
    variance_weighted_y: np.float64 = np.sum((Y - weighted_y_mean) ** 2 / (dY) ** 2) / weight_sum
    co_variance: np.float64 = np.sum((X - weighted_x_mean) * (Y - weighted_y_mean) / (dY) ** 2) / weight_sum

    print(co_variance)
    print(weighted_xy_mean - weighted_x_mean * weighted_y_mean)

    print("variance_weighted_x:", variance_weighted_x)
    print("variance_weighted_x:", weighted_xx_mean - weighted_x_mean**2)

    print("variance_weighted_xy:", co_variance)
    print("variance_weighted_xy:", weighted_xy_mean - weighted_x_mean * weighted_y_mean)

    alpha: np.float64 = (weighted_xx_mean * weighted_y_mean - weighted_x_mean * weighted_xy_mean) / (
        variance_weighted_x
    )
    beta: np.float64 = (weighted_xy_mean - weighted_x_mean * weighted_y_mean) / (
        weighted_xx_mean - weighted_x_mean**2
    )

    print("alpha:", alpha)

    print("beta: ", beta)
    print("beta: ", co_variance / variance_weighted_x)

    estimated_alpha_error: np.float64 = 1 / np.sqrt(variance_weighted_x) * np.sqrt(weighted_xx_mean / weight_sum)
    estimated_beta_error: np.float64 = 1 / np.sqrt(variance_weighted_x) / np.sqrt(weight_sum)

    print("estimated_alpha_error:", estimated_alpha_error)
    print("estimated_beta_error:", estimated_beta_error)


if __name__ == "__main__":
    main(sys.argv[1:])
