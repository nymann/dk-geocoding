from dk_geocoding.api import Api
from dk_geocoding.core.config import Config
from dk_geocoding.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
