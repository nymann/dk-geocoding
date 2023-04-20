from fastapi import FastAPI
from pogo_api.endpoint import Endpoint

from dk_geocoding.core.config import Config
from dk_geocoding.core.service_container import ServiceContainer
from dk_geocoding.endpoints.auto_complete import AutoComplete
from dk_geocoding.endpoints.geocoding import Geocoding
from dk_geocoding.endpoints.reverse_geocoding import ReverseGeocoding


class Api:
    def __init__(self, config: Config, service_container: ServiceContainer) -> None:
        self.api = FastAPI(version=config.version, title=config.title, docs_url="/")
        self.services = service_container
        self.add_endpoints()

    @property
    def endpoints(self) -> list[Endpoint]:
        return [Geocoding(), AutoComplete(), ReverseGeocoding()]

    def add_endpoints(self) -> None:
        for endpoint in self.endpoints:
            endpoint.route.add_to_router(self.api)
