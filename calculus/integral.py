import time

from numpy import double, arange, array
from functools import reduce


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        delta = end - start
        print(f'Function {func.__name__} was evaluated at {delta} secs!')
        return result
    return wrapper


class IntegralCalculation:
    eval_funcs = {}

    def __new__(cls, *args, **kwargs):
        cls.__add_methods()
        return super().__new__(cls)

    def __init__(self, limits=(0, 1), eval_step=0.001,
                 eval_method='rectangle', func=lambda x: x):
        self.eval_step = double(eval_step)
        self.eval_method = eval_method
        self.func = func
        self.limits = limits
        self.eval_error = None

    @classmethod
    def __add_methods(cls):
        cls.eval_funcs['rectangle'] = cls.__form_rectangle_method
        cls.eval_funcs['trapezoid'] = cls.__form_trapeziodal_method
        cls.eval_funcs['simpson'] = cls.__form_simpson_method

    @staticmethod
    def __form_rectangle_method(func_vals: array):
        result = reduce(lambda x, y: x + y, func_vals)
        return result

    @staticmethod
    def __form_trapeziodal_method(func_vals: array):
        length = len(func_vals)
        shift = 0
        result = 0
        while shift < length-2:
            result += (func_vals[shift]+func_vals[shift+1])/2
            shift += 1
        return result

    @staticmethod
    def __form_simpson_method(func_vals: array):
        length = len(func_vals)
        shift = 0
        result = 0
        while shift < length-3:
            result += \
                (func_vals[shift]+4*func_vals[shift+1]+func_vals[shift+2])/6
            shift += 1
        return result

    @time_decorator
    def evaluate_integral(self):
        a, b = self.limits
        end_num = double((b - a)) / self.eval_step
        counting_interval = arange(a, end_num) * self.eval_step
        func_values = self.func(counting_interval)
        if self.eval_method in self.eval_funcs.keys():
            eval_func = self.eval_funcs[self.eval_method]
            result = eval_func(func_values)
        else:
            raise ValueError('No such evaluation method!')
        return result*self.eval_step


if __name__ == '__main__':
    new_integral = IntegralCalculation(limits=(0, 1),
                                       eval_step=10**-8,
                                       func=lambda x: 4*(1-x**2)**0.5,
                                       eval_method='trapezoid')
    print(new_integral.evaluate_integral())
