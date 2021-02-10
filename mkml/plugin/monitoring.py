import inspect

from logzero import logger

from .base import BasePlugin


class MonitoringPlugin(BasePlugin):

    def apply(self, attrs, **kwargs):
        for m in attrs:
            func = attrs[m]
            if inspect.isfunction(func) or inspect.ismethod(func):
                logger.info(f'Start monitoring function {m}')
                attrs[m] = self._log(func)

