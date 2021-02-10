from .mkml_base import BaseModel
from .mkml_meta import MKMLMetaclass
from .plugin import StandardizationPlugin, MonitoringPlugin, LocalDataSourcePlugin, BasePlugin

MKMLMetaclass.register('standardization', StandardizationPlugin)
MKMLMetaclass.register('monitoring', MonitoringPlugin)
MKMLMetaclass.register('local_datasource', LocalDataSourcePlugin)
