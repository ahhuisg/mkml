import os
import pickle

from logzero import logger

from .base import BasePlugin


class LocalDataSourcePlugin(BasePlugin):

    def apply(self, attrs, **kwargs):
        logger.debug('Entering data source plugin')
        attrs['get_local_data'] = self._get_local_data

    def _get_local_data(self, feature_mart_location, group_id):
        feature_file = os.path.join(feature_mart_location, group_id+'.pkl')
        with open(feature_file, 'rb') as f:
            return pickle.load(f)
