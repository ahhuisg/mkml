from .base import BasePlugin


class StandardizationPlugin(BasePlugin):
    def __init__(self):
        self._standard_functions = ['fit', 'predict', 'score']

    def apply(self, attrs, **kwargs):
        for func_name in self._standard_functions:
            if func_name not in attrs:
                raise NotImplementedError(f'{func_name} must be presented in the class')
