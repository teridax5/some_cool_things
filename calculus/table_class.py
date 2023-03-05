class FunctionsForCalculus:
    def __init__(self, elementary=True, func_class='linear',
                 expression=lambda x: x):
        self.elementary = elementary
        self.func_class = func_class
        self.expression = expression

    def __eq__(self, other):
        result = (self.elementary, self.func_class), \
            (self.elementary, self.func_class)
        return result

    def __hash__(self):
        return hash((self.elementary, self.func_class))


class FunctionTable:
    def __init__(self):
        pass
