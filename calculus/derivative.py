from numpy import double, array, arange


class DerivativeCalculation:
    def __init__(self, eval_step=0.001, eval_point=0,
                 eval_func=lambda x: x):
        self.eval_step = double(eval_step)
        self.eval_func = eval_func
        self.eval_point = eval_point
        self.current_val = self.eval_func(self.eval_point)

    def __right_sided_derivative_calculation(self, point=None):
        if not point:
            point = self.eval_point
            self.current_val = self.eval_func(point)
        previous_val = self.eval_func(point-self.eval_step)
        return (self.current_val-previous_val)/self.eval_step

    def __left_sided_derivative_calculation(self, point=None):
        if not point:
            point = self.eval_point
            self.current_val = self.eval_func(point)
        next_val = self.eval_func(point+self.eval_step)
        return (next_val-self.current_val)/self.eval_step

    def eval_derivative(self, order=1, point=None):
        if not point:
            point = self.eval_point
        if order == 0:
            return self.current_val
        elif order == 1:
            result = (self.__left_sided_derivative_calculation(point) +
                      self.__right_sided_derivative_calculation(point)) / 2
            return result
        else:
            next_val = self.eval_derivative(
                order-1, point+self.eval_step
            )
            previous_val = self.eval_derivative(
                order-1, point-self.eval_step
            )
            return (next_val-previous_val)/(2*self.eval_step)


if __name__ == '__main__':
    new_derivative = DerivativeCalculation(eval_func=lambda x: x**3)
    print(new_derivative.eval_derivative(order=4))
