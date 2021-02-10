class MKMLMetaclass(type):

    plugins = {}

    @classmethod
    def register(cls, name, plugin_cls, *p_attrs, **p_kwargs):
        cls.plugins[name] = plugin_cls(*p_attrs, **p_kwargs)

    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)

        for _, plugin in cls.plugins.items():
            plugin.apply(attrs, **kwargs)

        return super().__new__(cls, name, bases, attrs, **kwargs)

