from .mkml_meta import MKMLMetaclass


class BaseModel(metaclass=MKMLMetaclass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def common_base_function(self):
        pass
