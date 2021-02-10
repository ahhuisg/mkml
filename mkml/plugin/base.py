import time

from logzero import logger


class BasePlugin(object):
    def _log(self, func):
        def wrapped(*args, **kwargs):
            try:
                start_time = time.time()
                logger.info(f"Entering ({func.__name__}) with parameters args: {args[1:]} - kwargs: {kwargs}")
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error(f'Exception in ({func.__name__}) : {e}')
                    raise e
            finally:
                end_time = time.time()
                logger.info(f"Exiting ({func.__name__}) with duration {end_time - start_time} seconds")
        return wrapped