from numpy import double, arange, array
from functools import reduce


class IntegralCalculation:
    def __init__(self, limits=(0, 1), eval_step=double(0.001),
                 eval_method='rectangle', func=lambda x: x):
        self.eval_step = eval_step
        self.eval_method = eval_method
        self.func = func
        self.limits = limits
        self.eval_error = None

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

    def evaluate_integral(self):
        a, b = self.limits
        end_num = double((b - a)) / self.eval_step
        counting_interval = arange(a, end_num) * self.eval_step
        func_values = self.func(counting_interval)



