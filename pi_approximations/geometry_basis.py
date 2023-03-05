from time import time
from random import uniform
from numpy import double, array, arange


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        delta = end - start
        print(f'Function {func.__name__} was evaluated at {delta} secs!')
        return result
    return wrapper


@time_decorator
def pi_approximation_v1(n):
    circle_points = square_points = 0
    for _ in range(n):
        x = uniform(0, 1)
        y = uniform(0, 1)
        if x**2 + y**2 <= 1:
            circle_points += 1
        square_points += 1
    return 4*(circle_points/square_points)


def circle_point_finder(x: array) -> array:
    return (1-x**2)**0.5


@time_decorator
def pi_approximation_v2(n):
    step = double(1/n)
    x_array = arange(1, n+1, dtype=double)*step
    circle_points = circle_point_finder(x_array)
    circle_ver_strips_areas = step*circle_points
    return round(circle_ver_strips_areas.sum()*4, 11)


if __name__ == '__main__':
    num = 10**8
    print(pi_approximation_v2(num))
