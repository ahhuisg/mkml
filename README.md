# mkml

mkml implements a Microkernel Architecture for Machine Learning Library

Medium post is at [here](https://yanhui79.medium.com/microkernel-architecture-for-machine-learning-library-c04b797e0d5f)

# try it out

* Install from PyPi

```python
pip install mkml
```

* By default, 3 Plug-in modules have been loaded

```python
MKMLMetaclass.register('standardization', StandardizationPlugin)
MKMLMetaclass.register('monitoring', MonitoringPlugin)
MKMLMetaclass.register('local_datasource', LocalDataSourcePlugin)
```

**StandardizationPlugin** enforces the method signatures of the model class. In our case, the model class must have **fit**, **predict** and **score** methods

**MonitoringPlugin** monitors all the functions of the model class. In our case, it logs the input parameters, exception as well as the duration of each function in the model class

**LocalDataSourcePlugin** helps loading the data locally. It dynamically ingest data-loading functions into the model class to help data scientist retrieve the data without worrying how to retrieve it

* Create your own model

```python
from sklearn.linear_model import LinearRegression
from mkml import BaseModel

class UserModel(BaseModel):
    def __init__(self):
        self._model = LinearRegression()
        
    def fit(self, features, labels):
        self._model.fit(X_train, y_train)

    def predict(self, features):
        self._model.predict(features)

    def score(self, features, labels):
        return self._model.score(features, labels)
```

* Instantiate the model class instance and load features and labels for training and prediction 
```python
um = UserModel()

features = um.get_local_data(feature_mart_location='data', group_id='train_features')
labels = um.get_local_data(feature_mart_location='data', group_id='train_labels')

um.fit(features, labels)

test_features = um.get_local_data(feature_mart_location='data', group_id='test_features')
test_labels = um.predict(test_features)
```

* Create and register your own Plug-in Module (ie. Remote DataSource)

```python
from mkml import BasePlugin

class RemoteDataSourcePlugin(BasePlugin):
	
    def __init__(self, name):
        self._name = name
    
    def apply(self, attrs, **kwargs):
        logger.debug('Entering data source plugin')
        attrs['get_remote_data'] = self._get_remote_data
    
    def _get_remote_data(self, feature_mart_location, group_id):
        # To be implemented
        pass


## You can add additional instantiation parameters to the Plug-in class as well	
MKMLMetaclass.register('remote_datasource', RemoteDataSourcePlugin, 'remote_ds_plugin')
```

* Use the new Remote DataSource Plug-in to retrieve features and labels

```python
um = UserModel()

features = um.get_remote_data(feature_mart_location='http://fm', group_id='train_features')
labels = um.get_remote_data(feature_mart_location='http://fm', group_id='train_labels')
```
